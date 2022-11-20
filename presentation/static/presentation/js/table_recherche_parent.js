$(document).ready(function() {

// Ajout du champ du champ de recherche ************************
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
// Fin de recherche **************************************************


// ******************* GESTION DES AFFICHAGES DES CHAMPS POUR AJOUTER UN PARENT *****************************

    var btn_p_ajouter = $('#btn_p_ajouter');
    var btn_p_annuler = $('#btn_p_annuler');
    var select_typeparent = $('#select_typeparent');
    var nomprenoms = $('#input[name=nomprenoms]');
    var datenaissance = $('#input[name=datenaissance]');
    var contact = $('#input[name=contact]');
    var trouver = true;

    // Traitement AJAX
    btn_p_ajouter.click(function(e){
            e.preventDefault(); // On annule l'envoi du formulaire

            if(!select_typeparent.val()){
                trouver = false;
                alert('Veuillez sélectionner le type de parent.');
                select_typeparent.focus();
            }else if(!nomprenoms.val()){
                trouver = false;
                alert('Veuillez sélectionner le type de parent.');
                nomprenoms.focus();
            }else{
                trouver = true;
            }

            if(trouver){
                // On utilise ajax pour transmetre les données
                $.ajax({
                    url: "/vieprofessionnelle/ajouter-parent", // On ajoute l'url absolue en commençant par la racine
                    type: 'POST',
                    data: {
                        id_json: $('#id_json').val(),
                        select_typeparent: select_typeparent.val(),
                        nomprenoms: nomprenoms.val(),
                        datenaissance: datenaissance.val(),
                        adresse: adresse.val(),
                        contact: contact.val(),
                        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                    },
                    success: function(data){

                        // On remplit les champs
                        parent_liste.append("")

                        // Gestion des fermetures des boutons
                        btn_p_annuler.trigger('click'); // On initialise les champs
                    },
                    statusCode: {
                        404: function(data){
                                alert('Veuillez renseigner les champs SVP.');
                             },
                    },
                });
            }



        });

    // Partie : GESTION DU TABLEAU PARENT

    var liens_parent = $("#table_recherche_parent tbody td a");
        liens_parent.each(function(){

            $(this).click(function(){
                // On remplit les champs
                 parent_liste.append("<option value='"+ $(this).attr('value') +"' selected>" + $(this).text() + "</option>")
                 parent_l_fermer.trigger('click'); // On ferme le modal de la recherche
            });

        });


// *****************************************************************************

} );