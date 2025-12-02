try:
    from puzzle_02_raw_list import RAW_EXAMPLE_LIST, FIRST_PUZZLE_LIST
except ImportError:
    RAW_EXAMPLE_LIST = []
    FIRST_PUZZLE_LIST = []


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

        # Early break - no symmetrical odd lengths
        if not id_len % 2 == 0:
            return

        chars = [l for l in id_as_str]

        for char in chars:
            char_occurs = chars.count(char)
            if char_occurs > 1 and char != 1:
                symmetry_at = int(id_len / 2)
                if id_as_str[0:symmetry_at] == id_as_str[symmetry_at:]:
                    self.candidates.add(_id)

            # originally misread instructions to include 999, 11111, etc.
            # if char_occurs == id_len: # perfect repeated pattern
            #     self.candidates.add(_id)

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
    using_raw_example_list = IdRange.build_id_ranges(RAW_EXAMPLE_LIST)
    print(IdRange.summarize_ranges(using_raw_example_list))

    using_first_puzzle_list = IdRange.build_id_ranges(FIRST_PUZZLE_LIST)
    print(IdRange.summarize_ranges(using_first_puzzle_list))

main()
