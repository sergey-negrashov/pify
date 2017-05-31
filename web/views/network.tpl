<button type="button" data-target="#{{ssid.lower().replace(" ", "_")}}" class="list-group-item list-group-item-action" data-toggle="collapse" aria-expanded="false" aria-controls="{{ssid.lower().replace(" ", "_")}}">
    {{ssid}}
    <span class="float-right text-right">
        <span class="icon-wifi3"></span>
    </span>
</button>
<div class="collapse" id="{{ssid.lower().replace(" ", "_")}}">
    <div class="card card-block">
        <p><b>SSID:</b> {{ssid}}</p>
        <p><b>Security:</b> {{security}}</p>
        <p><b>Signal Strength:</b> {{strength}}%</p>
        <form>
            <div class="form-group row">
                <input type="password" class="form-control col-sm-10" id="{{ssid.lower().replace(" ", "_")}}pass" placeholder="Network Password">
                <button type="submit" class="btn btn-primary col-sm-2">Connect to Network</button>
            </div>
        </form>
    </div>
</div>