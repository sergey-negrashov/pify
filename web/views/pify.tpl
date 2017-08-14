<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="css/bootstrap.min.css" />

    <link rel="stylesheet" href="css/pifi.css">
    <title>{{pify_server_title}}</title>
</head>
<body>
<nav class="navbar navbar-inverse bg-inverse sticky-top">
    <a class="navbar-brand" href="#">{{pify_server_title}}</a>
</nav>
<div class="container" id="content">
    <div class="row">
        <div class="col-sm-12">
            <div class="card">
                <div class="card-header">
                    Available Wireless Networks
                </div>
                <div class="card-block">
                    <ul class="list-group">
                    % for network in sorted(networks, key=lambda lst: lst[2], reverse=True):
                        %include("web/views/network.tpl", ssid=network[0].decode("utf-8"), security=network[1], strength=network[2])
                    % end

                    <!-- Connect to hidden open network -->
                    <button type="button" data-target="#hidden-open" class="list-group-item list-group-item-action" data-toggle="collapse" aria-expanded="false" aria-controls="hidden-open">
                        Connect to Hidden Open Network
                        <span class="icon-plus"></span>
                    </button>
                    <div class="collapse" id="hidden-open">
                        <div class="card card-block">
                            <form action="/connect/open" method="POST">
                                <input id="security_type_open" name="security_type" type="hidden" value="open">
                                <div class="form-group row">
                                    <input type="text" class="form-control col-sm-10" id="open-network-ssid" name="ssid" placeholder="Open Network SSID">
                                    <button type="submit" class="btn btn-primary col-sm-2">Connect to Network</button>
                                </div>
                            </form>
                        </div>
                    </div>

                    <!-- Connect to hidden WPA network -->
                    <button type="button" data-target="#hidden-wpa" class="list-group-item list-group-item-action" data-toggle="collapse" aria-expanded="false" aria-controls="hidden-wpa">
                        Connect to Hidden WPA Network
                        <span class="icon-plus"></span>
                    </button>
                    <div class="collapse" id="hidden-wpa">
                        <div class="card card-block">
                            <form action="/connect/wpa" method="POST">
                                <input id="security_type_wpa" name="security_type" type="hidden" value="wpa">
                                <div class="form-group row">
                                    <input type="text" class="form-control col-sm-5" id="wpa-network-ssid" name="ssid" placeholder="WPA Network SSID">
                                    <input type="password" class="form-control col-sm-5" id="wpa-network-pass" name="ssid_pass" placeholder="WPA Network Password">
                                    <button type="submit" class="btn btn-primary col-sm-2">Connect to Network</button>
                                </div>
                            </form>
                        </div>
                    </div>
                    </ul>
                </div>
                <div class="card-footer">
	    	    <!--<a href="/refresh" class="btn btn-danger btn-block">Refresh Wireless Network List</a>-->
                    <a href="/forget" class="btn btn-danger btn-block">Forget Saved Networks</a>
                </div>
            </div>
        </div>
    </div>
</div>



<!-- jQuery first, then Tether, then Bootstrap JS. -->
<script src="js/jquery-3.1.1.slim.min.js"></script>
<script src="js/tether.min.js"></script>
<script src="js/bootstrap.min.js"></script>
<script type="text/javascript">
    $(document).ready(function(){
        $('.collapse').on('show.bs.collapse', function (e) {
            $('.collapse').collapse("hide")
        })
    })
</script>
</body>
</html>
