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
            <div class="contact-form">
                <div class="form-title">Question</div>
                
                <form method="post" action="URL of sent.php">
                    <div class="form-item">name</div>
                    <input type="text" name="name">

                    <div class="form-title">age</div>
                    <select name="age">
                        <option value="no-selection">Please select!</option>
                        <?php
                            for($i=6; $i<=100; $i++){
                                echo "<option value='{$i}'>{$i}</option>";
                            }
                        ?>
                    </select>

                    <div class="form-item">The type of asking</div>
                    <?php
                        $types = array('AskOfProgate', 'OpinionOfProgate', 'AskOfRecruit', 'TVinterview', 'Money', 'Other');
                    ?>
                    <select name="category">
                        <option value="no-selection">Please select!</option>
                        <?php
                            foreach($types as $type){
                                echo "<option value='{$type}'>{$type}</option>";
                            }
                        ?>
                    </select>

                    <div class="form-item">contents</div>
                    <textarea name="body"></textarea>

                    <input type="submit" value="sent">
                </form>
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