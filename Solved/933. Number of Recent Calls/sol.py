class RecentCounter:
    def __init__(self):
        self.pings = []
        self.range = 3000

    def ping(self, t: int) -> int:
        self.pings.append(t)
        recent_ping_time = t - self.range
        recent_ping_counter = 0
        for ping in self.pings[::-1]:
            if ping >= recent_ping_time:
                recent_ping_counter += 1
            else:
                break
        return recent_ping_counter


if __name__ == "__main__":
    rc = RecentCounter()
    pings = [1, 100, 3001, 3002]
    for ping in pings:
        print(rc.ping(ping))
