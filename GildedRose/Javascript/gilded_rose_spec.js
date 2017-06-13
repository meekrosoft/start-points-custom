'use strict';

var gr = require('./gilded_rose.js');

describe("Gilded Rose", function() {

  it("should foo", function() {
    const gildedRose = new gr.Shop([ new gr.Item("foo", 0, 0) ]);
    const items = gildedRose.updateQuality();
    expect(items[0].name).toEqual("fixme");
  });

});
