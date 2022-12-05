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
    var colonneparent = [0,1,2,3,4,5];

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


//******************** SCRIPT DE L'ONGLET TYPE ETAT DE SANTE **********************************************
     // Ajout du champ du champ de recherche
    var tabletypeetatsante = "tabletypeetatsante";
    var colonnetypeetatsante = [0,1];

    //$('#' + tabletypeetatsante + ' thead tr').clone(true).addClass('filters').appendTo( '#' + tabletypeetatsante + ' thead' );
    var table5 = $('#' + tabletypeetatsante ).DataTable( {

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
            columns: colonnetypeetatsante,
        },
    },

    { // Boutton de excel
        extend:'excel',
        text: '<i class="fas fa-file-excel"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'Excel',
        // Option pour le choix des colonnes a afficher
        exportOptions:{
            columns: colonnetypeetatsante,
        },
    },

    { // Boutton PDF
        extend:'pdf',
        text: '<i class="fas fa-file-pdf"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'PDF',
        exportOptions:{
            columns: colonnetypeetatsante,
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
            columns: colonnetypeetatsante,
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


//******************** SCRIPT DE L'ONGLET TYPE ETAT DE SANTE **********************************************
     // Ajout du champ du champ de recherche
    var tabletypedocument = "tabletypedocument";
    var colonnetypedocument = [0,1];

    //$('#' + tabletypedocument + ' thead tr').clone(true).addClass('filters').appendTo( '#' + tabletypedocument + ' thead' );
    var table6 = $('#' + tabletypedocument ).DataTable( {

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
            columns: colonnetypedocument,
        },
    },

    { // Boutton de excel
        extend:'excel',
        text: '<i class="fas fa-file-excel"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'Excel',
        // Option pour le choix des colonnes a afficher
        exportOptions:{
            columns: colonnetypedocument,
        },
    },

    { // Boutton PDF
        extend:'pdf',
        text: '<i class="fas fa-file-pdf"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'PDF',
        exportOptions:{
            columns: colonnetypedocument,
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
            columns: colonnetypedocument,
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


//******************** SCRIPT DE L'ONGLET CHAPEAU **********************************************
    var tablechapeau = "tablechapeau";
    var colonnechapeau = [0,1,2,3];

    var table7 = $('#' + tablechapeau ).DataTable( {

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
            columns: colonnechapeau,
        },
    },

    { // Boutton de excel
        extend:'excel',
        text: '<i class="fas fa-file-excel"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'Excel',
        // Option pour le choix des colonnes a afficher
        exportOptions:{
            columns: colonnechapeau,
        },
    },

    { // Boutton PDF
        extend:'pdf',
        text: '<i class="fas fa-file-pdf"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'PDF',
        exportOptions:{
            columns: colonnechapeau,
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
            columns: colonnechapeau,
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

 //******************** SCRIPT DE L'ONGLET TYPE DE PERSONNE RESSOURCE **********************************************
    var tabletypepersonneressource = "tabletypepersonneressource";
    var colonnetypepersonneressource = [0,1];

    var table8 = $('#' + tabletypepersonneressource ).DataTable( {

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
            columns: colonnetypepersonneressource,
        },
    },

    { // Boutton de excel
        extend:'excel',
        text: '<i class="fas fa-file-excel"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'Excel',
        // Option pour le choix des colonnes a afficher
        exportOptions:{
            columns: colonnetypepersonneressource,
        },
    },

    { // Boutton PDF
        extend:'pdf',
        text: '<i class="fas fa-file-pdf"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'PDF',
        exportOptions:{
            columns: colonnetypepersonneressource,
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
            columns: colonnetypepersonneressource,
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

 //******************** SCRIPT DE L'ONGLET PERSONNE RESSOURCE **********************************************
    var tablepersonneressource = "tablepersonneressource";
    var colonnepersonneressource = [0,1,2,3];

    var table9 = $('#' + tablepersonneressource ).DataTable( {

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
            columns: colonnepersonneressource,
        },
    },

    { // Boutton de excel
        extend:'excel',
        text: '<i class="fas fa-file-excel"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'Excel',
        // Option pour le choix des colonnes a afficher
        exportOptions:{
            columns: colonnepersonneressource,
        },
    },

    { // Boutton PDF
        extend:'pdf',
        text: '<i class="fas fa-file-pdf"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'PDF',
        exportOptions:{
            columns: colonnepersonneressource,
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
            columns: colonnepersonneressource,
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

 //******************** SCRIPT DU MODULE AJOUTER PERSONNE RESSOURCE **********************************************
    var table_recherche_personneressource = "table_recherche_personneressource";
    var colonnerecherche_personneressource = [0,1,2];

    var table10 = $('#' + table_recherche_personneressource ).DataTable( {

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
            columns: colonnerecherche_personneressource,
        },
    },

    { // Boutton de excel
        extend:'excel',
        text: '<i class="fas fa-file-excel"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'Excel',
        // Option pour le choix des colonnes a afficher
        exportOptions:{
            columns: colonnerecherche_personneressource,
        },
    },

    { // Boutton PDF
        extend:'pdf',
        text: '<i class="fas fa-file-pdf"></i>',
        className: 'btn btn-secondary',
        titleAttr: 'PDF',
        exportOptions:{
            columns: colonnerecherche_personneressource,
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
            columns: colonnerecherche_personneressource,
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
    $('#recherche_personneressource').keyup(function(){
        table10.search($(this).val()).draw();
    });

// ******************* GESTION DE LA SUPPRESSION D'UNE PERSONNE RESSOURCE *****************************
    tablepersonneressource = $('#tablepersonneressource');

    function supprimer_ligne_personneressouce(){
        var supprimer_p = $('button[name=supprimer_p]');
        var annuler_p = $('button[name=annuler_p]');

        // Traitement AJAX
        supprimer_p.each(function(){
            $(this).click(function(e){
                e.preventDefault();

                // On utilise ajax pour transmettre les données
                $.ajax({
                    url: "vieprofessionnelle/supprimer-personneressource/", // On ajoute l'url absolue en commençant par la racine
                    type: 'get',
                    data: {
                        supprimer_p: $(this).val(),
                    },
                    success: function(data){

                        // On vide le contenu
                        tablepersonneressource.html('');

                        // On remplit les champs
                        $.each(data.data, function(k, valeur){
                            k++; // On incrémente la variable à chaque fois pour avoir le nombre exacte car la variable débute par 0
                            tablepersonneressource.append(`

                                <tr>
                                    <td>` + k + `</td>
                                    <td>` + valeur.type.type + `</td>
                                    <td>` + valeur.chapeau ? valeur.chapeau.chapeau : valeur.membre.nom_prenoms + `</td>
                                    <td>` + valeur.chapeau ? valeur.chapeau.contact : valeur.membre.contact + `</td>
                                    <td class="text-center">
                                        <button type="button" title="Supprimer" class="btn btn-outline-danger btn-sm" data-toggle="modal" data-target="#personneressourcesupprimermodal` + valeur.id + `" data-backdrop="static"><i class="fas fa-trash-alt"></i></button>
                                        <!-- Modal -->
                                        <div class="modal fade" id="personneressourcesupprimermodal` + valeur.id + `" role="dialog">
                                            <div class="modal-dialog">

                                                <!-- Modal content-->
                                                <div class="modal-content">
                                                    <div class="modal-header">
                                                        <h4 class="modal-title">Confirmez-vous la suppression ?</h4>
                                                        <button type="button" class="close" data-dismiss="modal">&times;</button>
                                                    </div>
                                                    <div class="modal-body">
                                                        <h5>
                                                            Personne ressource : <strong>` + valeur.type.type + `</strong>
                                                        </h5>
                                                    </div>
                                                    <div class="modal-footer justify-content-center">

                                                        <form style="display:inline-block; text-align:center" method="get" action="#">
                                                            <button type="submit" name="supprimer_p" value="` + valeur.id + `" class="btn btn-success btn-sm">Oui</button>
                                                        </form>
                                                        <button class="btn btn-danger btn-sm" name="annuler_p" data-dismiss="modal">Non</button>

                                                    </div>
                                                </div>

                                            </div>
                                        </div>
                                        <!-- Modal Fin -->
                                    </td>
                                </tr>

                            `);

                        });

                        annuler_p.trigger('click');

                        // Affichage du toast ---------
                        var btn = $('#btn_ferme_toast_suppression');
                        var toast = $('#mytoast_suppression');
                            toast.addClass('show');
                            btn.click(function(){
                                toast.removeClass('show');
                            });
                         var montemps = setInterval(function(){
                            toast.removeClass('show');
                            clearInterval(montemps);
                         }, 3000);
                         // Fin toast -----------

                        // On appelle la fonction pour prendre en compte tous les changement des lignes supprimées
                        supprimer_ligne_personneressouce();
                    },
                    statusCode: {
                        404: function(data){
                                alert('Veuillez réessayer car une erreur est survenue.');
                             },
                    },
                });

            });
        });
    }

    supprimer_ligne_personneressouce(); // On appelle la fonction

// ******************* GESTION DE L'AJOUT D'UNE PERSONNE RESSOURCE A PARTIR DU TABLEAU DE RECHERCHE ***

var liste_btn_ajouter = $('#tablepersonneressource tbody button');
var typepersonneressource = $('#select_typepersonneressource')

    liste_btn_ajouter.each(function(){

        $(this).click(function(e){
            e.preventDefault();

            // On utilise ajax pour transmettre les données
            $.ajax({
                    url: "vieprofessionnelle/ajouter-personneressource", // On ajoute l'url absolue en commençant par la racine
                    type: 'GET',
                    data: {
                        typepersonneressource: typepersonneressource.val(),
                        id: $(this).val(),
                    },
                    success: function(data){

                        // On vide le contenu
                        tablepersonneressource.html("");

                        // On remplit les champs
                        $.each(data.data, function(k, valeur){
                            k++; // On incrémente la variable à chaque fois pour avoir le nombre exacte car la variable débute par 0
                            tablepersonneressource.append(`

                                <tr>
                                    <td>` + k + `</td>
                                    <td>` + valeur.type.type + `</td>
                                    <td>` + valeur.chapeau ? valeur.chapeau.chapeau : valeur.membre.nom_prenoms + `</td>
                                    <td>` + valeur.chapeau ? valeur.chapeau.contact : valeur.membre.contact + `</td>
                                    <td class="text-center">
                                        <button type="button" title="Supprimer" class="btn btn-outline-danger btn-sm" data-toggle="modal" data-target="#personneressourcesupprimermodal` + valeur.id + `" data-backdrop="static"><i class="fas fa-trash-alt"></i></button>
                                        <!-- Modal -->
                                        <div class="modal fade" id="personneressourcesupprimermodal` + valeur.id + `" role="dialog">
                                            <div class="modal-dialog">

                                                <!-- Modal content-->
                                                <div class="modal-content">
                                                    <div class="modal-header">
                                                        <h4 class="modal-title">Confirmez-vous la suppression ?</h4>
                                                        <button type="button" class="close" data-dismiss="modal">&times;</button>
                                                    </div>
                                                    <div class="modal-body">
                                                        <h5>
                                                            Personne ressource : <strong>` + valeur.type.type + `</strong>
                                                        </h5>
                                                    </div>
                                                    <div class="modal-footer justify-content-center">

                                                        <form style="display:inline-block; text-align:center" method="get" action="#">
                                                            <button type="submit" name="supprimer_p" value="` + valeur.id + `" class="btn btn-success btn-sm">Oui</button>
                                                        </form>
                                                        <button class="btn btn-danger btn-sm" name="annuler_p" data-dismiss="modal">Non</button>

                                                    </div>
                                                </div>

                                            </div>
                                        </div>
                                        <!-- Modal Fin -->
                                    </td>
                                </tr>

                            `);
                        });

                        // Affichage du toast ---------
                        var btn = $('#btn_ferme_toast_success');
                        var toast = $('#mytoast_success');
                            toast.addClass('show');
                            btn.click(function(){
                                toast.removeClass('show');
                            });
                         var montemps = setInterval(function(){
                            toast.removeClass('show');
                            clearInterval(montemps);
                         }, 3000);
                         // Fin toast -----------

                        supprimer_ligne_personneressouce(); // On appelle la fonction pour prendre en compte les nouvelles données

                    },
                    statusCode: {
                        404: function(data){
                                alert('Veuillez renseigner les champs SVP.');
                             },
                    },
                });
        });

    });


// FIN -----------------------------
} );