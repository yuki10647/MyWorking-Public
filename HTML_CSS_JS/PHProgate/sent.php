<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Progate</title>
        <link rel="stylesheet" type="text/css" href="stylesheet.css">
    </head>
    
    <body>
        <div class="header">
            <div class="header-left">Progate</div>

            <div class="header-right">
                <ul>
                    <li>country-information</li>
                    <li>recruitment</li>
                    <li class="selected">question</li>
                </ul>
            </div>
        </div>

        <div class="main">
            <div class="thanks-masseage">Thank you for asking!</div>
            <div class="display-contact">
                <div class="form-title">ContentsOfInput</div>

                <div class="form-item">>name</div>
                <?php
                    echo $_POST['name'];
                ?>

                <div class="form-item">>age</div>
                <?php
                    echo $_POST['age'];
                ?>

                <div class="form-item">>type of question</div>
                <?php
                    echo $_POST['category'];
                ?>

                <div class="form-item">>contents</div>
                <?php
                    echo $_POST['body'];
                ?>
            </div>
        </div>

        <div class="footer">
            <div class="footer-left">
                <ul>
                    <li>country-information</li>
                    <li>recruitment</li>
                    <li>question</li>
                </ul>
            </div>

            <div class="like-box">
                <iframe src="URLofImage"></iframe>
            </div>
        </div>
    </body>
</html>        
