$(document).ready(function() {

//******************** SCRIPT DE L'ONGLET TYPE SECTEUR **********************************************
     // Ajout du champ du champ de recherche
    var tabletypesecteur = "tabletypesecteur";
    var colonneypesecteur = [0,1];

    //$('#' + tabletypesecteur + ' thead tr').clone(true).addClass('filters').appendTo( '#' + tabletypesecteur + ' thead' );
    var table1 = $('#' + tabletypesecteur ).DataTable( {

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

    // Désactiver le trie d'un ou de plusieurs colonnes
    /*"columnDefs":[{
        "targets":4, // [4,5]
        "orderable":false,
    }],*/

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
            columns: colonneypesecteur,
        },
    },

    { // Boutton de excel
        extend:'excel',
        text: '<i class="fas fa-file-excel"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'Excel',
        // Option pour le choix des colonnes a afficher
        exportOptions:{
            columns: colonneypesecteur,
        },
    },

    { // Boutton PDF
        extend:'pdf',
        text: '<i class="fas fa-file-pdf"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'PDF',
        exportOptions:{
            columns: colonneypesecteur,
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
            columns: colonneypesecteur,
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

//******************** SCRIPT DE L'ONGLET SECTEUR **********************************************
     // Ajout du champ du champ de recherche
    var tablesecteur = "tablesecteur";
    var colonnesecteur = [0,1];

    //$('#' + tablesecteur + ' thead tr').clone(true).addClass('filters').appendTo( '#' + tablesecteur + ' thead' );
    var table2 = $('#' + tablesecteur ).DataTable( {

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

    // Désactiver le trie d'un ou de plusieurs colonnes
    /*"columnDefs":[{
        "targets":4, // [4,5]
        "orderable":false,
    }],*/

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
            columns: colonnesecteur,
        },
    },

    { // Boutton de excel
        extend:'excel',
        text: '<i class="fas fa-file-excel"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'Excel',
        // Option pour le choix des colonnes a afficher
        exportOptions:{
            columns: colonnesecteur,
        },
    },

    { // Boutton PDF
        extend:'pdf',
        text: '<i class="fas fa-file-pdf"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'PDF',
        exportOptions:{
            columns: colonnesecteur,
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
            columns: colonnesecteur,
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



//******************** SCRIPT DE L'ONGLET TYPE DE PARENT **********************************************
     // Ajout du champ du champ de recherche
    var tabletypeparent = "tabletypeparent";
    var colonnetypeparent = [0,1];

    //$('#' + tabletypeparent + ' thead tr').clone(true).addClass('filters').appendTo( '#' + tabletypeparent + ' thead' );
    var table3 = $('#' + tabletypeparent ).DataTable( {

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

    // Désactiver le trie d'un ou de plusieurs colonnes
    /*"columnDefs":[{
        "targets":4, // [4,5]
        "orderable":false,
    }],*/

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
            columns: colonnetypeparent,
        },
    },

    { // Boutton de excel
        extend:'excel',
        text: '<i class="fas fa-file-excel"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'Excel',
        // Option pour le choix des colonnes a afficher
        exportOptions:{
            columns: colonnetypeparent,
        },
    },

    { // Boutton PDF
        extend:'pdf',
        text: '<i class="fas fa-file-pdf"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'PDF',
        exportOptions:{
            columns: colonnetypeparent,
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
            columns: colonnetypeparent,
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


//******************** SCRIPT DE L'ONGLET PARENT **********************************************
     // Ajout du champ du champ de recherche
    var tableparent = "tableparent";
    var colonneparent = [0,1,2,3];

    //$('#' + tableparent + ' thead tr').clone(true).addClass('filters').appendTo( '#' + tableparent + ' thead' );
    var table4 = $('#' + tableparent ).DataTable( {

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

    // Désactiver le trie d'un ou de plusieurs colonnes
    /*"columnDefs":[{
        "targets":4, // [4,5]
        "orderable":false,
    }],*/

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
            columns: colonneparent,
        },
    },

    { // Boutton de excel
        extend:'excel',
        text: '<i class="fas fa-file-excel"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'Excel',
        // Option pour le choix des colonnes a afficher
        exportOptions:{
            columns: colonneparent,
        },
    },

    { // Boutton PDF
        extend:'pdf',
        text: '<i class="fas fa-file-pdf"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'PDF',
        exportOptions:{
            columns: colonneparent,
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
            columns: colonneparent,
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


} );