import os
import pathlib
import unittest

if os.environ.get("RUNFILES_FROM_RULES_PYTHON") == "1":
    from python import runfiles  # "@rules_python//python/runfiles"
else:
    import runfiles  # requirement("bazel-runfiles")


class RunfilesTest(unittest.TestCase):
    def test_runfiles(self) -> None:
        r = runfiles.Runfiles.Create()
        path = pathlib.Path(r.Rlocation("_main/runfiles_from_pipy_do_not_work/test_data.txt"))
        self.assertEquals(path.read_text(), "42\n")


if __name__ == "__main__":
    unittest.main()
