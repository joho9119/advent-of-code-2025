from textwrap import wrap
try:
    from puzzle_02_raw_list import RAW_EXAMPLE_LIST, REAL_PUZZLE_LIST

except ImportError:
    RAW_EXAMPLE_LIST = []
    REAL_PUZZLE_LIST = []


class IdRange:
    def __init__(self, start: int, end: int):
        self.start, self.end = start, end
        self.candidates: set[int] = set()
        self._register_candidates()
        
    def _register_candidates(self):
        # incrementing to ensure whole range
        for _id in range(self.start, self.end + 1):
            self._register_potential_dupes(_id)

    def _register_potential_dupes(self, _id: int):

        id_as_str = str(_id)
        id_len = len(id_as_str)
        midpoint = id_len // 2

        for i in range(midpoint):
            substrings = wrap(id_as_str, i+1)
            for sub in substrings:
                if all(sub == s for s in substrings):
                    self.candidates.add(_id)
                    return

    def show_candidates(self):
        if self.candidates:
            print(f"Candidates found in range {self.start} => {self.end}")
            print(self.candidates)
        else:
            print(f"No candidates found in range {self.start} => {self.end}")

    @classmethod
    def build_id_ranges(cls, id_list: str | list[str]) -> list[IdRange]:
        ids = id_list.split(",")

        out: list[cls] = []
        for rng_str in ids:
            start, end = rng_str.strip().split("-")
            out.append(cls(int(start), int(end)))
        return out

    @classmethod
    def summarize_ranges(cls, rng_list: list[IdRange]) -> int:
        candidates = []
        for r in rng_list:
            candidates.extend(list(r.candidates))
        return sum(candidates)

def main():
    # using_raw_example_list = IdRange.build_id_ranges(RAW_EXAMPLE_LIST)
    # for r in using_raw_example_list:
    #     r.show_candidates()
    # print(IdRange.summarize_ranges(using_raw_example_list))

    using_puzzle_list= IdRange.build_id_ranges(REAL_PUZZLE_LIST)
    for r in using_puzzle_list:
        r.show_candidates()
    print(IdRange.summarize_ranges(using_puzzle_list))

main()
