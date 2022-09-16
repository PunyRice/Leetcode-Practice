from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.key = ''
        self.values = defaultdict(list)  # keys: a dict of many values with its corresponding time stamps


    def set(self, key: str, value: str, timestamp: int) -> None:
        left, right = 0, len(self.values[key])-1


        if self.values[key][right][1] <= timestamp:
            self.values[key][right].append([value,timestamp])

        elif self.values[key][left][1] >= timestamp:
            self.values[key][left].append([value,timestamp])

        else:
        # timestamp is target
            while left <= right:
                mid = left+((right-left) // 2)
                if self.values[key][mid][1] > timestamp:  # index 1 because 0 is string and 1 is timestamp
                    right = mid + 1

                elif self.values[key][mid][1] < timestamp:
                    left = mid + 1
                else:
                    print(f"equallllllllll, {left},{right}")  # same value found
                    self.values[key][mid].append([value,timestamp])
                    break
        self.values[key].append([value, timestamp])

        print(self.values)

        return

    def get(self, key: str, timestamp: int) -> str:

        return


if __name__ == "__main__":
    print("ass")
    obj = TimeMap()
    obj.set("bongo","bass",2)
    obj.set("bongo","bink",1)
    obj.set("bongo","back",8)
    #param_2 = obj.get(key,timestamp)


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)