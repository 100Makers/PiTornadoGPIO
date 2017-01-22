var main : Main = null;

class Main{
    constructor(){
        this.websocket = new WebSocket('ws://'+window.location.hostname+':'+window.location.port+'/websocket');

        this.websocket.onmessage = (event : MessageEvent) => { this.onMessageReceived(event); };
        this.websocket.onopen = () => { this.onConnectionOpen(); };
        this.websocket.onclose = () => { this.onConnectionClosed(); };
        this.websocket.onerror = () => { this.onError(); };
    }

    public sendMessage(message:string) : void {
        this.websocket.send(message)
    }

    private onMessageReceived(event : MessageEvent) : void {
        console.log("messaggio ricevuto");
        console.log(event.data);
    }

    private onConnectionOpen() : void {
        console.log("connessione effettuata");
    }

    private onConnectionClosed() : void {
        console.log("connessione chiusa");
    }

    private onError() : void {
        console.log("errore nella connessione");
    }

    private websocket : WebSocket = null;
}


window.onload = () => {
    main = new Main();
};
