class Solution:
    def nodesBetweenCriticalPoints(self, head):
        ans = [-1, -1]

        prev = head
        curr = head.next

        pos = 1
        first = -1
        last = -1
        min_dist = float('inf')

        while curr.next:
            nxt = curr.next

            # Check if curr is a critical point
            if ((curr.val > prev.val and curr.val > nxt.val) or
                (curr.val < prev.val and curr.val < nxt.val)):

                if first == -1:
                    # First critical point
                    first = pos
                else:
                    # Distance from previous critical point
                    min_dist = min(min_dist, pos - last)

                last = pos

            prev = curr
            curr = nxt
            pos += 1

        # Fewer than 2 critical points
        if first == -1 or first == last:
            return [-1, -1]

        # Maximum distance = last - first
        max_dist = last - first

        return [min_dist, max_dist]
