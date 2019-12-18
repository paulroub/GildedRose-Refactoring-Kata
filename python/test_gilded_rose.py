# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_normal_quality_decay(self):
        items = [Item("foo", 7, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(49, items[0].quality)
        self.assertEqual(6, items[0].sell_in)

    def test_double_quality_decay_after_sell_by(self):
        items = [Item("foo", 0, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(48, items[0].quality)

    def test_increasing_cheese_quality(self):
        items = [Item("Aged Brie", 5, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].quality)

    def test_cheese_quality_capped(self):
        items = [Item("Aged Brie", 5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_quality_cant_be_negative(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_backstage_passes_increase_more_than_ten_days_sell_by(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].quality)

    def test_backstage_passes_increase_quality_twice_between_six_and_ten_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 6, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(3, items[0].quality)

    def test_backstage_passes_increase_quality_thrice_between_one_and_five_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].quality)

    def test_backstage_passes_no_value_after_sell_by_date(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_sulfuras_never_changes(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)
        self.assertEqual(10, items[0].sell_in)

    def test_unexpired_conjured_item_degrades_twice_as_fast(self):
        items = [Item("Conjured", 10, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(38, items[0].quality)

    def test_expired_conjured_item_degrades_twice_as_fast(self):
        items = [Item("Conjured", 0, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(36, items[0].quality)

    def test_unexpired_conjured_item_cant_degrade_below_zero(self):
        items = [Item("Conjured", 0, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

if __name__ == '__main__':
    unittest.main()
