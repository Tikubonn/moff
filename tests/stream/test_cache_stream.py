
from unittest import TestCase
from moff.stream import CacheStream
from io import StringIO


class TestCacheStream (TestCase):

    def test_peek1(self):
        with StringIO("abc") as stream:
            cstream = CacheStream(stream)
            self.assertEqual(cstream.peek(), "a")
            self.assertEqual(cstream.peek(), "a")
            self.assertEqual(cstream.peek(), "a")

    def test_get1(self):
        with StringIO("abc") as stream:
            cstream = CacheStream(stream)
            self.assertEqual(cstream.get(), "a")
            self.assertEqual(cstream.get(), "b")
            self.assertEqual(cstream.get(), "c")

    def test_get2(self):
        with StringIO("abc") as stream:
            cstream = CacheStream(stream)
            self.assertEqual(cstream.peek(), "a")
            self.assertEqual(cstream.get(), "a")
            self.assertEqual(cstream.peek(), "b")
            self.assertEqual(cstream.get(), "b")
            self.assertEqual(cstream.peek(), "c")
            self.assertEqual(cstream.get(), "c")

    def test_read1(self):
        with StringIO("abc") as stream:
            cstream = CacheStream(stream)
            self.assertEqual(cstream.read(3), "abc")

    def test_release1(self):
        with StringIO("abc") as stream:
            cstream = CacheStream(stream)
            read1 = cstream.read(3)
            self.assertEqual(read1, "abc")
            cstream.release(read1)
            read2 = cstream.read(3)
            self.assertEqual(read2, "abc")

    def test_release2(self):
        with StringIO("abc") as stream:
            cstream = CacheStream(stream)
            read = cstream.read(3)
            self.assertEqual(read, "abc")
            cstream.release(read)
            self.assertEqual(cstream.get(), "a")
            self.assertEqual(cstream.get(), "b")
            self.assertEqual(cstream.get(), "c")
