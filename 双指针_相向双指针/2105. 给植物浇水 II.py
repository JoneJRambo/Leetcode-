class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        left = 0
        right = len(plants) - 1
        a = capacityA
        b = capacityB
        count = 0
        while left <= right:
            if left == right:
                if a < b:
                    if b < plants[left]:
                        b = capacityB
                        count += 1
                    b -= plants[left]
                else:
                    if a < plants[left]:
                        a = capacityA
                        count += 1
                    a -= plants[left]
            else:
                if a < plants[left]:
                    a = capacityA
                    count += 1
                a -= plants[left]
                if b < plants[right]:
                    b = capacityB
                    count += 1
                b -= plants[right]

            left += 1
            right -= 1