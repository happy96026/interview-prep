class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minuteAngle = 360 / 60 * minutes
        hourAngle = (hour % 12 * 360 + minuteAngle) / 12
        angle = abs(minuteAngle - hourAngle)
        return min(angle, 360 - angle)


def main():
    s = Solution()
    print(s.angleClock(12, 30))
    print(s.angleClock(3, 30))
    print(s.angleClock(3, 15))
    print(s.angleClock(4, 50))
    print(s.angleClock(12, 0))

if __name__ == '__main__':
    main()