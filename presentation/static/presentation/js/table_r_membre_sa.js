$(document).ready(function() {

    // Ajout du champ du champ de recherche
    var table_recherche_membre = "table_recherche_membre";
    var colonnerecherche = [0,1,2,3,4,5,6];
    var table = $('#' + table_recherche_membre ).DataTable( {

    // Pagination du tableau
    // Paramètres optionnels du DATATABLES
    paging: true,
    pageLength: 10,
    lengthChange: true,
    autoWidth: true,
    searching : true,
    bInfo : true,
    bSort : true,
    select : true,
    order : [],

    // Gestion de l'affichage de la langue des champs
        language: {
        processing:     "Traitement en cours...",
        search:         "Rechercher&nbsp;:",
        lengthMenu:    "Afficher _MENU_ &eacute;l&eacute;ments",
        info:           "Affichage de l'&eacute;lement _START_ &agrave; _END_ sur _TOTAL_ &eacute;l&eacute;ments",
        infoEmpty:      "Affichage de l'&eacute;lement 0 &agrave; 0 sur 0 &eacute;l&eacute;ments",
        infoFiltered:   "(filtr&eacute; de _MAX_ &eacute;l&eacute;ments au total)",
        infoPostFix:    "",
        loadingRecords: "Chargement en cours...",
        zeroRecords:    "Aucun &eacute;l&eacute;ment &agrave; afficher",
        emptyTable:     "Aucune donnée disponible dans le tableau",
        paginate: {
            first:      "Premier",
            previous:   "Pr&eacute;c&eacute;dent",
            next:       "Suivant",
            last:       "Dernier"
        },
        aria: {
            sortAscending:  ": activer pour trier la colonne par ordre croissant",
            sortDescending: ": activer pour trier la colonne par ordre décroissant"
        }
    },

    // Gestion des Bouttons Copie, export excel, PDF, impression
        dom:'lBfrtip',
        buttons: [

        { // Boutton de copie
            extend:'copy',
            text: '<i class="fas fa-clone"></i>',
            className: 'btn btn-secondary',
            titleAttr: 'Copier',
            // Option pour le choix des colonnes a afficher
            exportOptions:{
                columns: colonnerecherche,
            },
        },

        { // Boutton de excel
            extend:'excel',
            text: '<i class="fas fa-file-excel"></i>',
            className: 'btn btn-secondary',
            titleAttr: 'Excel',
            // Option pour le choix des colonnes a afficher
            exportOptions:{
                columns: colonnerecherche,
            },
        },

        { // Boutton PDF
            extend:'pdf',
            text: '<i class="fas fa-file-pdf"></i>',
            className: 'btn btn-secondary',
            titleAttr: 'PDF',
            exportOptions:{
                columns: colonnerecherche,
            },

            tableHeader: {
                alignment: 'center',
            },

            customize: function (doc){
                doc.styles.tableHeader.alignment = 'center'; // Alignement du titre
                doc.styles.tableBodyOdd.alignment = 'center'; // Alignement des lignes en couleur
                doc.styles.tableBodyEven.alignment = 'center'; // Alignement des lignes blanches
                doc.styles.tableHeader.fontSize = 7 ; // Taille de l'entête du tableau
                doc.defaultStyle.fontSize = 6 ; // Taille du contenu du tableau

                // Centrer le tableau dans le document
                doc.content[1].table.widths = Array(doc.content[1].table.body[1].length + 1).join('*').split('');
            },

        },

        { // Boutton Imprimer
            extend:'print',
            text: '<i class="fas fa-print"></i>',
            className: 'btn btn-secondary',
            titleAttr: 'Imprimer',
            // Option pour le choix des colonnes a afficher
            exportOptions:{
                columns: colonnerecherche,
            },

            // Personnalisation de l'affichage
            customize: function(win){
                $(win.document.body).css('font-size', '10pt')
                $(win.document.body).find('table')
                .addClass('compact')
                .css('font-size', 'inherit');
            },
        },

        ],

            // Fin de pagination

    } );

    // Recherche globale du tableau
    var monTableau = $('#'+ table_recherche_membre).DataTable(); // On récupère le tableau
    $('#recherche_membre').keyup(function(){
        monTableau.search($(this).val()).draw();
    });
     //Fin de recherche


} );