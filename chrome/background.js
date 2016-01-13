chrome.omnibox.onInputChanged.addListener(
  function(text, suggest) {
    console.log('inputChanged: ' + text);
    // suggest([{content:'lol',description:'negrumps'}]);
    $.get('http://localhost:5000/signin', {username: "lit", password: "lit" }, function(data) {
        suggest([{content: "hello", description: data}]);
    });
    // suggest([
    //   {content: text + " one", description: "the first one"},
    //   {content: text + " number two", description: "the second entry"}
    // ]);
  });

// This event is fired with the user accepts the input in the omnibox.
chrome.omnibox.onInputEntered.addListener(
  function(text) {
    console.log('inputEntered: ' + text);
    alert('You just typed "' + text + '"');
  });
