<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="css/bootstrap.min.css" />

    <link rel="stylesheet" href="css/pifi.css">
</head>
<body>
<nav class="navbar navbar-inverse bg-inverse sticky-top">
    <a class="navbar-brand" href="#">PiFi Wireless Agent - OPQ</a>
</nav>
<div class="container" id="content">
    <div class="row">
        <div class="col-sm-12">
            Pify is attempting to connect to ({{ssid}}).<br />
            This process takes 30 seconds.<br />
            Please do not attempt to refresh this page.<br />
            <br /><br />
            <div id="countdown">This page will redirect in 30 seconds...</div>
        </div>
    </div>
</div>

<!-- jQuery first, then Tether, then Bootstrap JS. -->
<script src="js/jquery-3.1.1.slim.min.js"></script>
<script src="js/tether.min.js"></script>
<script src="js/bootstrap.min.js"></script>
<script type="text/javascript">
    var countdown = 30; // Seconds
    var one_sec = 1000; // Milliseconds
    function cd() {
        countdown--;
        document.getElementById("countdown").innerText = "This page will refresh in " + countdown + " seconds..."
        if(countdown > 0) {
            window.setTimeout(cd, one_sec);
        } else {
            //window.location.href = "http://10.0.0.1"
        }
    }
    cd();
</script>
</body>
</html>
