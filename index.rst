.. container:: grid

    .. container:: grid-23

        .. container:: aligncenter

            .. image:: _images/haum-session-de-travail.jpg

            .. image:: _images/viens-au-haum.png

    .. container:: grid-13

        .. raw:: html

            <h2>Actualités</h2>
            <h3>À venir</h3>
            <div id=calendar></div><div class=clearer>&nbsp;</div>
            <script type="text/javascript" src="_static/calendar.js"></script>
            <script type="text/javascript">
                events.forEach(function (e){
                    $('#calendar').append(
                        '<div class=event><div class=dateheure><p class=date><span>'+e.date[0]+'</span> '+e.date[1]+' '+e.date[2]+'</p><p class=heure>'+
                        e.date[3]+':'+e.date[4]+'</p></div><p class=lieu>'+e.lieu+'</p><p class=descr>'+e.texte+'</p></div>'
                    );
                });
            </script>
            <h3>Fil twitter</h3>
            <a class="twitter-timeline" href="https://twitter.com/haum72" data-widget-id="454141251034427392" data-chrome="nofooter">Suivre @haum72 sur Twitter</a>
            <script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src="//platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script>
