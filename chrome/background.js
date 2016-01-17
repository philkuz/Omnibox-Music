var server = 'http://localhost:5000'
var google_songs;
var signed_in = false;
function regex_letter(c){
    /*
    Returns regex pattern that will match both the uppercase and the lowercase
    of letter c. The parameter must already be a character, otherwise
    the function will fail
    */
    // determine if the letter is uppercase or lowercase
    if (c == c.toUpperCase()){
        return '['+c+c.toLowerCase()+']'
    }
    else{
        return '['+c+c.toUpperCase()+']'
    }
}
function regex(string) {
    regexed = ""
    for(var i = 0; i < string.length; i++){
        var c = string.charAt(i)
        if (/\W/g.test(c) == false) {
            regexed += regex_letter(c)
        }
        else {
            regexed += c
        }
    }

    return new RegExp(regexed)
}
function search(query, callback){
    if(google_songs == undefined){
        callback(false)
    }
    regexed = regex(query)


}
function google_sign_in(user, pwd){
    $.post(server+'/sign_in', {username: user, password: pwd}, function(result) {
        get_google_songs()
    });
    //; $.ajax({
    //     url: server+'/sign_in',
    //     type: 'POST',
    //     data:
    //     success: function(result) {
    //         get_google_songs()
    //     }
    // });
}
function get_google_songs() {
    $.get(server+'/gmusic', function(data){
        if (data === 'not_signed_in'){
            console.log('not signed into google music')
        }
        else{
            google_songs = JSON.parse(data)
            console.log(google_songs)
        }
    });
}

function sign_in_suggestion(){
    return {content:'sign_in_link', description: 'Sign in to google music through this link'}
}
chrome.omnibox.onInputChanged.addListener(
  function(text, suggest) {
    console.log('inputChanged: ' + text);
    // suggest([{content:'lol',description:'negrumps'}]);
    search(text, function(value){
        if(value == false){
            suggest([sign_in_suggestion()])
        }
        else{

        }
    });
    $.get('http://localhost:5000/search', {query: text}, function(data) {
        if (data === 'not_signed_in'){
            suggest([{content:'no', description:'lit'}])
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
function search(){}
function song_formatter(title, artist){
    return title + ' by ' + artist;
}
// This event is fired with the user accepts the input in the omnibox.
chrome.omnibox.onInputEntered.addListener(
  function(text) {
    console.log('inputEntered: ' + text);
    alert('You just typed "' + text + '"');
  });
