class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0

        total_duration = 0

        for i in range(len(timeSeries) - 1):
            gap = timeSeries[i + 1] - timeSeries[i]
            total_duration += min(gap, duration)

        # Add the duration of the last attack
        total_duration += duration

        return total_duration
