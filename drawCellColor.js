function assignCellColors() {
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    var rValues = sheet.getRange("P3:P93").getValues();
    var gValues = sheet.getRange("Q3:Q93").getValues();
    var bValues = sheet.getRange("R3:R93").getValues();
    var colorRange = sheet.getRange("S3:S93");
    
    var colors = [];
    
    for (var i = 0; i < rValues.length; i++) {
      var r = rValues[i][0];
      var g = gValues[i][0];
      var b = bValues[i][0];
      
      var hexColor = rgbToHex(r, g, b);
      colors.push([hexColor]);
    }
    
    colorRange.setBackgrounds(colors);
  }
  
  function rgbToHex(r, g, b) {
    r = Math.floor(r);
    g = Math.floor(g);
    b = Math.floor(b);
    
    var hexR = r.toString(16).padStart(2, '0');
    var hexG = g.toString(16).padStart(2, '0');
    var hexB = b.toString(16).padStart(2, '0');
    
    return "#" + hexR + hexG + hexB;
  }
  