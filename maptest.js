/* 

EXAMPLE DATA

var doc = {
    "date": "2015-12-20-14-55-43", 
    "day": 20, 
    "hour": 14, 
    "minute": 55, 
    "month": 12, 
    "second": 43, 
    "temperature": 22.5, 
    "year": 2015
}
*/

// VIEW: temp_by_hour
// URI: DATABASE_URI/_design/DOCUMENT_FOLDER/_view/temp_by_hour?group_level=1
// MAP
function(doc) {
  if (doc.date) {

    if (doc.month < 10) {
      var month = "0".concat(doc.month.toString());
    }
    else {
      var month = doc.month.toString();
    }

    if (doc.day < 10) {
      var day = "0".concat(doc.day.toString());
    }
    else {
      var day = doc.day.toString();
    }

    if (doc.hour < 10) {
      var hour = "0".concat(doc.hour.toString());
    }
    else {
      var hour = doc.hour.toString();
    }
    var day_hour = doc.year.toString()
                       .concat("-")
                       .concat(month)
                       .concat("-")
                       .concat(day)
                       .concat("-")
                       .concat(hour);
    emit(day_hour, doc.temperature);
  }
}

// REDUCE
function (key, value) {
  return sum(value);
}

// VIEW: count_by_hour
// URI: /DATABASE_URI/_design/DOCUMENT_FOLDER/_view/count_by_hour?group_level=1
// MAP
function(doc) {
  if (doc.date) {

    if (doc.month < 10) {
      var month = "0".concat(doc.month.toString());
    }
    else {
      var month = doc.month.toString();
    }

    if (doc.day < 10) {
      var day = "0".concat(doc.day.toString());
    }
    else {
      var day = doc.day.toString();
    }

    if (doc.hour < 10) {
      var hour = "0".concat(doc.hour.toString());
    }
    else {
      var hour = doc.hour.toString();
    }
    var day_hour = doc.year.toString()
                       .concat("-")
                       .concat(month)
                       .concat("-")
                       .concat(day)
                       .concat("-")
                       .concat(hour);
    emit(day_hour, 1);
  }
}

// REDUCE
function (key, value) {
  return sum(value);
}