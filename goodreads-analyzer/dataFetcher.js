// Scrape the data from the GoodReads website
//
// Source URL:
//
//   http://www.goodreads.com/genres/list


//=========================================================================
// Just fetch the numbers (does not depend on jQuery)
//=========================================================================


// var output = '';
// var books = document.getElementsByClassName('smallText');

// for (var i = 0; i < books.length; ++i) {
//   output += books[i].innerHTML.replace(/\b books\b/, '').replace(/\n/, '');
// };

// if (copy) {
//   // Depends on Firebug's `copy' function
//   copy(output);
// } else if (console.log) {
//   // Depends on any `console.log' function (e.g. Firebug's one)
//   console.log(output);
// } else {
//   output;
// }

//=========================================================================
// Fetch genre titles + numbers (depends on jQuery)
//=========================================================================

// When used with jQueryfy bookmarklet
var $ = jQuery;

$(document).ready(function() {


  var data = [];

  /* Removes leading and trailing whitespace fron a string
   *
   * @string - Arbitrary string.
   *
   * Returns a string without leading or trailing whitespace
   */
  var cleanString = function(string) {
    var s = string.replace(/^\s*/, '');
    return s.replace(/\s*$/, '');
  }

  $('.shelfStat').each(function(e, i) {
    data.push([cleanString($(this).find('.mediumText').text()),
               cleanString($(this).find('.smallText').text()).replace(
                   / books$/, '').replace(',', '')]);
  });

  // console.log(JSON.stringify(data, undefined, 2));



  // Make a CSV string
  var csv = '';
  for (var i = 0; i < data.length; ++i) {
    csv += data[i][1] + ',' + data[i][0] + '\n';
  }

  copy(csv);

});

