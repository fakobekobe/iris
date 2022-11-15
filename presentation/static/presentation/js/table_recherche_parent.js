$(document).ready(function() {

    // Ajout du champ du champ de recherche
    var table_recherche_parent = "table_recherche_parent";
    var table = $('#' + table_recherche_parent ).DataTable( {

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

    } );

    // Recherche globale du tableau
    var monTableau = $('#'+ table_recherche_parent).DataTable(); // On récupère le tableau
    $('#recherche_parent').keyup(function(){
        monTableau.search($(this).val()).draw();
    });
     //Fin de recherche


} );