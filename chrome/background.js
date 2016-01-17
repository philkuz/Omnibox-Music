chrome.omnibox.onInputChanged.addListener(
  function(text, suggest) {
    console.log('inputChanged: ' + text);
    // suggest([{content:'lol',description:'negrumps'}]);
    $.get('http://localhost:5000/search', {query: text}, function(data) {
        if (data === 'not_signed_in'){
            suggest({content:'', description:'you need to sign in'})
        }
        else{
            matches = JSON.parse(data);
            suggestions = [];
            for (var i = 0;  i < matches.length; i++) {

                suggestions.push({content: matches['url'], description: song_formatter(matches['title'], matches['artist'])});
            }
            suggest(suggestions)
        }
    });
    // suggest([
    //   {content: text + " one", description: "the first one"},
    //   {content: text + " number two", description: "the second entry"}
    // ]);
  });
function search()
function song_formatter(title, artist){
    return title + ' by ' + artist;
}
// This event is fired with the user accepts the input in the omnibox.
chrome.omnibox.onInputEntered.addListener(
  function(text) {
    console.log('inputEntered: ' + text);
    alert('You just typed "' + text + '"');
  });
