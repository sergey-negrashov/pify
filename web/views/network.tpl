<button type="button" data-target="#{{ssid.lower().replace(" ", "_")}}" class="list-group-item list-group-item-action" data-toggle="collapse" aria-expanded="false" aria-controls="{{ssid.lower().replace(" ", "_")}}">
    {{ssid}}
    % if strength < 25:
    <span class="icon-wifi0"></span>
    % elif strength < 50:
    <span class="icon-wifi1"></span>
    % elif strength < 75:
    <span class="icon-wifi2"></span>
    % else:
    <span class="icon-wifi3"></span>
    % end
</button>
<div class="collapse" id="{{ssid.lower().replace(" ", "_")}}">
    <div class="card card-block">
        <p><b>SSID:</b> {{ssid}}</p>
        <p><b>Security:</b> {{"Open" if security == 0 else "WPA"}}</p>
        <p><b>Signal Strength:</b> {{strength}}%</p>
        <form>
            <div class="form-group row">
            % if security == 0:
                <button type="submit" class="btn btn-primary btn-block">Connect to Network</button>
            % else:
                <input type="password" class="form-control col-sm-10" id="{{ssid.lower().replace(" ", "_")}}pass" placeholder="Network Password">
                <button type="submit" class="btn btn-primary col-sm-2">Connect to Network</button>
            % end
            </div>
        </form>
    </div>
</div>