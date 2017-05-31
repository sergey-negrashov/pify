<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="css/bootstrap.min.css"
          integrity="sha384-rwoIResjU2yc3z8GV/NPeZWAv56rSmLldC3R/AZzGRnGxQQKnKkoFVhFQhNUwEyJ" crossorigin="anonymous">

    <link rel="stylesheet" href="css/pifi.css">
</head>
<nav class="navbar navbar-inverse bg-inverse sticky-top">
    <a class="navbar-brand" href="#">PiFi Wireless Agent - OPQ</a>
</nav>
<body>
<div class="container" id="content">
    <div class="row">
        <div class="col-sm-12">
            <div class="card">
                <div class="card-header">
                    Available Wireless Networks
                </div>
                <div class="card-block">
                    <ul class="list-group">
                    % for network in networks:
                        %include("network.tpl", ssid=network[0], security=network[1], strength=network[2])
                    % end

                    </ul>

                </div>
                <div class="card-footer">
                    <button type="button" class="btn btn-danger btn-block">Refresh Wireless Network List</button>
                </div>
            </div>
        </div>
    </div>
</div>



<!-- jQuery first, then Tether, then Bootstrap JS. -->
<script src="js/jquery-3.1.1.slim.min.js"
        integrity="sha384-A7FZj7v+d/sdmMqp/nOQwliLvUsJfDHW+k9Omg/a/EheAdgtzNs3hpfag6Ed950n"
        crossorigin="anonymous"></script>
<script src="js/tether.min.js"
        integrity="sha384-DztdAPBWPRXSA/3eYEEUWrWCy7G5KFbe8fFjk5JAIxUYHKkDx6Qin1DkWx51bBrb"
        crossorigin="anonymous"></script>
<script src="js/bootstrap.min.js"
        integrity="sha384-vBWWzlZJ8ea9aCX4pEW3rVHjgjt7zpkNpZk+02D9phzyeVkE+jo0ieGizqPLForn"
        crossorigin="anonymous"></script>
</body>
</html>