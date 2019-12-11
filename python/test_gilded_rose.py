# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_normal_quality_decay(self):
        items = [Item("foo", 7, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(49, items[0].quality)
        self.assertEquals(6, items[0].sell_in)

    def test_double_quality_decay_after_sell_by(self):
        items = [Item("foo", 0, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(48, items[0].quality)

    def test_increasing_cheese_quality(self):
        items = [Item("Aged Brie", 5, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(2, items[0].quality)

    def test_cheese_quality_capped(self):
        items = [Item("Aged Brie", 5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)

    def test_quality_cant_be_negative(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)

if __name__ == '__main__':
    unittest.main()
