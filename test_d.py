import unittest, dupehunt, tempfile, pathlib
class T(unittest.TestCase):
    def test(self):
        d=pathlib.Path(tempfile.mkdtemp()); (d/"a").write_text("igual"); (d/"b").write_text("igual"); (d/"c").write_text("outro")
        g=dupehunt.achar(str(d)); self.assertEqual(len(g),1); self.assertEqual(len(g[0]),2); self.assertTrue((d/"a").exists())
unittest.main()
