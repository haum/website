.. used for titles inside of columns
.. role:: faketitle

.. container:: aligncenter

    .. image:: _images/viens-au-haum.png
        :width: 600px

.. raw:: html

    <div id=calendar></div><div class=clearer>&nbsp;</div>

.. raw:: html

    <script type="text/javascript" src="_static/calendar.js"></script> <script type="text/javascript">
        events.forEach(function (e){
            $('#calendar').append(
                '<div class=event><div class=dateheure><p class=date><span>'+e.date[0]+'</span> '+e.date[1]+' '+e.date[2]+'</p><p class=heure>'+
                e.date[3]+':'+e.date[4]+'</p></div><p class=lieu>'+e.lieu+'</p><p class=descr>'+e.texte+'</p></div>'
            );
        });
    </script>

.. container:: twocolumns

    .. container:: left

        :faketitle:`A propos de nous`


        .. toctree::
           :maxdepth: 1

           le_projet
           planet
           rencontres
           hackerland

        :faketitle:`En public...`

          - `Conférences Libres`_

    .. container:: right

        :faketitle:`Les projets`

        .. toctree::
            :maxdepth: 2

            projets

.. container:: clearer

    |clearer|

.. _Conférences Libres: /confs_libres.html

.. |clearer| unicode:: U+0020 .. space


