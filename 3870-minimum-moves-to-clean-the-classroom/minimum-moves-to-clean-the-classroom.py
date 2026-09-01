from collections import deque


class Solution:
    def minMoves(self, classroom, energy):
        m = len(classroom)
        n = len(classroom[0])

        # Find starting position and litter cells
        sr = sc = -1
        litter = []

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    sr, sc = r, c
                elif classroom[r][c] == 'L':
                    litter.append((r, c))

        k = len(litter)

        if k == 0:
            return 0

        # Give each litter cell a bit
        litter_id = [[-1] * n for _ in range(m)]

        for i, (r, c) in enumerate(litter):
            litter_id[r][c] = i

        full_mask = (1 << k) - 1

        # best[r][c][mask] = maximum energy remaining
        # with which we reached this state
        best = [
            [
                [-1] * (1 << k)
                for _ in range(n)
            ]
            for _ in range(m)
        ]

        # (row, col, mask, remaining_energy)
        q = deque()
        q.append((sr, sc, 0, energy))

        best[sr][sc][0] = energy

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        moves = 0

        while q:
            for _ in range(len(q)):
                r, c, mask, rem = q.popleft()

                if mask == full_mask:
                    return moves

                if rem == 0:
                    continue

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue

                    if classroom[nr][nc] == 'X':
                        continue

                    # Moving costs 1 energy
                    nrem = rem - 1
                    nmask = mask

                    # Collect litter
                    if litter_id[nr][nc] != -1:
                        nmask |= 1 << litter_id[nr][nc]

                    # Reset energy at R
                    if classroom[nr][nc] == 'R':
                        nrem = energy

                    # Already reached this state with >= energy
                    if best[nr][nc][nmask] >= nrem:
                        continue

                    best[nr][nc][nmask] = nrem
                    q.append((nr, nc, nmask, nrem))

            moves += 1

        return -1
