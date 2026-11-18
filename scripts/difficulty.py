"""Fetch per-problem solve counts from contest.ucup.ac standings (overseas stages only).

Standings pages embed `problems=[...]`, `score={team: {index: [points, ...]}}` and
`standings=[[total, penalty, team, rank, ...], ...]`. A problem counts as solved by a
team when its points reach 100. Difficulty is solved teams / teams with at least one
solve; it is measured data, not an estimated CF rating.

Raw pages are cached in sources/ (gitignored). Use --refresh to refetch.
"""
import json, re, sys, time, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UA = 'UCup-topic-study/1.0 (personal training archive; overseas allowlist)'
FULL = 100


def contest_id(stage):
    m = re.search(r'/contest/(\d+)/problem/', stage['problems'][0]['url'])
    return m.group(1) if m else None


def fetch(cid, refresh):
    cache = ROOT / 'sources' / f'standings-{cid}.html'
    if cache.exists() and not refresh:
        return cache.read_text(encoding='utf-8')
    req = urllib.request.Request(f'https://contest.ucup.ac/contest/{cid}/standings', headers={'User-Agent': UA})
    with urllib.request.urlopen(req, timeout=180) as r:
        text = r.read().decode('utf-8')
    cache.write_text(text, encoding='utf-8')
    time.sleep(1.5)
    return text


def parse(text):
    """Return ({problem_id: solved_teams}, active_teams, total_teams)."""
    probs = json.loads(re.search(r'\bproblems=(\[[^\]]*\]);', text).group(1))
    score = json.loads(re.search(r'\nscore=(\{.*?\});\n', text, re.S).group(1))
    stand = json.loads(re.search(r'\nstandings=(\[.*?\]);\n', text, re.S).group(1))
    solved = [0] * len(probs)
    for row in score.values():
        if isinstance(row, dict):  # teams with no submissions are serialized as []
            for idx, cell in row.items():
                if cell[0] >= FULL:
                    solved[int(idx)] += 1
    active = sum(1 for r in stand if r[0] > 0)
    return {str(p): solved[i] for i, p in enumerate(probs)}, active, len(stand)


def main():
    refresh = '--refresh' in sys.argv
    stages = [s for s in json.loads((ROOT / 'data/stages.json').read_text()) if s['policy'] == 'overseas']
    out, errors = {}, []
    for st in stages:
        cid = contest_id(st) if st.get('problems') else None
        if not cid:
            errors.append(dict(stage_id=st['id'], error='no contest id'))
            continue
        try:
            solved, active, total = parse(fetch(cid, refresh))
        except Exception as exc:  # keep going; record the gap instead of writing zeros
            errors.append(dict(stage_id=st['id'], contest=cid, error=f'{type(exc).__name__}: {exc}'[:200]))
            continue
        probs = {}
        for p in st['problems']:
            pid = p['url'].rsplit('/', 1)[1]
            if pid in solved:
                probs[p['letter']] = solved[pid]
        out[st['id']] = dict(contest=cid, active_teams=active, total_teams=total, solved=probs,
                             unmatched=sorted(set(solved) - {p['url'].rsplit('/', 1)[1] for p in st['problems']}))
        print(st['id'], cid, f'active={active}', f'matched={len(probs)}/{len(st["problems"])}', flush=True)
    data = dict(source='https://contest.ucup.ac/contest/<id>/standings', solved_threshold=FULL,
                fetched=time.strftime('%Y-%m-%d'), stages=out, errors=errors)
    (ROOT / 'data/difficulty.json').write_text(json.dumps(data, ensure_ascii=False, indent=2))
    print('stages', len(out), 'errors', len(errors))


if __name__ == '__main__':
    main()
