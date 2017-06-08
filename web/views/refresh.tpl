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
            Pify has exited AP mode in order to scan for additional nearby WiFi networks.<br />
            This process takes 30 seconds.<br />
            Please do not attempt to refresh this page.<br />
            The SSID list will reappear when Pify has completed refreshing...<br /><br />
            <div id="countdown">This page will refresh in 30 seconds...</div>
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
            window.location.href = "/"
        }
    }
    cd();
</script>
</body>
</html>
