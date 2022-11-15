$(document).ready(function(){

// ******************* GESTION DES LISTES DEROULANTES *****************************

    var niveau = $('select[name=niveau]');
    var niveauscolaire = $('select[name=niveauscolaire]');

    // Traitement AJAX du niveau
    niveau.change(function(){

            // On utilise ajax pour récupérer les niveaux
            $.ajax({
                url: "/presentation/details-niveauscolaire", // On ajoute l'url absolue en commençant par la racine
                type: 'get',
                data: {
                    id: $(this).val(),
                },
                success: function(data){
                    // On initialise la selection du niveau scolaire
                    niveauscolaire.html('');
                    niveauscolaire.append("<option value='' selected>--- Selectionnez un niveau scolaire ---</option>");

                    $.each(data.data, function(key, value){
                        niveauscolaire.append("<option value='" + value.id + "' >" + value.libelle + "</option>");
                    });
                },
            });


        });


// ******************* GESTION DES AFFICHAGES DES CHAMPS POUR AJOUTER UN PARENT *****************************
    var parent_annuler = $('#parent_annuler');
    var parent_liste = $('#parent_liste');
    var btn_p_ajouter = $('#btn_p_ajouter');
    var btn_p_annuler = $('#btn_p_annuler');
    var btn_p_fermer = $('#btn_p_fermer');

    parent_annuler.click(function(){
        parent_liste.html('');
    });

    // Traitement AJAX
    btn_p_ajouter.click(function(e){
            e.preventDefault(); // On annule l'envoi du formulaire

            // On utilise ajax pour transmetre les données
            $.ajax({
                url: "/vieprofessionnelle/ajouter-parent", // On ajoute l'url absolue en commençant par la racine
                type: 'post',
                data: {
                    id_json: $('#id_json').val(),
                    select_typeparent: $('#select_typeparent').val(),
                    nomprenoms: $('input[name=nomprenoms]').val(),
                    select_typeparent: $('#select_typeparent').val(),
                    datenaissance: $('input[name=datenaissance]').val(),
                    adresse: $('input[name=adresse]').val(),
                    contact: $('input[name=contact]').val(),
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                },
                success: function(data){

                    // On remplit les champs
                    parent_liste.append("<option value='"+ data.data.id +"' selected>" + data.data.nomprenoms + "</option>")

                    // Affichage du message
                    alert(data.data.message);

                    // Gestion des fermetures des boutons
                    btn_p_annuler.trigger('click'); // On initialise les champs du modal en cours
                    btn_p_fermer.trigger('click'); // On ferme le modal en cours
                    //cooperative_l_fermer.trigger('click'); // On ferme le modal de la recherche
                },
                statusCode: {
                    404: function(data){
                            alert('Veuillez renseigner les champs SVP.');
                         },
                },
            });


        });


// ******************* GESTION DES LISTES DEROULANTES *****************************

    var select_district = $('select[name=select_district]');
    var select_region = $('select[name=select_region]');
    var select_departement = $('select[name=select_departement]');
    var select_ville = $('select[name=select_ville]');
    var select_commune = $('select[name=select_commune]');

        // Traitement AJAX de la region
        $(select_district).change(function(){

            // On utilise ajax pour récupérer les régions
            $.ajax({
                url: "/localisation/details-region", // On ajoute l'url absolue en commençant par la racine
                type: 'get',
                data: {
                    id: $(this).val(),
                },
                success: function(data){
                    // On initialise la selection de la région
                    select_region.html('');
                    select_region.append("<option value='' selected>--- Selectionnez une région ---</option>");

                    // On initialise la selection du département
                    select_departement.html('');
                    select_departement.append("<option value='' selected>--- Selectionnez un département ---</option>");

                    // On initialise la selection du ville
                    select_ville.html('');
                    select_ville.append("<option value='' selected>--- Selectionnez une ville ---</option>");

                    // On initialise la selection de la commune
                    select_commune.html('');
                    select_commune.append("<option value='' selected>--- Selectionnez une commune ---</option>");

                    $.each(data.data, function(key, value){
                        select_region.append("<option value='" + value.id + "' >" + value.libelle + "</option>");
                    });
                },
            });


        });

        // Traitement AJAX du departement
        $(select_region).change(function(){

            // On utilise ajax pour récupérer les départements
            $.ajax({
                url: "/localisation/details-departement", // On ajoute l'url absolue en commençant par la racine
                type: 'get',
                data: {
                    id: $(this).val(),
                },
                success: function(data){
                    // On initialise la selection du département
                    select_departement.html('');
                    select_departement.append("<option value='' selected>--- Selectionnez un département ---</option>");

                    // On initialise la selection du ville
                    select_ville.html('');
                    select_ville.append("<option value='' selected>--- Selectionnez une ville ---</option>");

                    // On initialise la selection de la commune
                    select_commune.html('');
                    select_commune.append("<option value='' selected>--- Selectionnez une commune ---</option>");

                    $.each(data.data, function(key, value){
                        select_departement.append("<option value='" + value.id + "' >" + value.libelle + "</option>");
                    });
                },
            });


        });

        // Traitement AJAX de la ville
        $(select_departement).change(function(){

            // On utilise ajax pour récupérer les villes
            $.ajax({
                url: "/localisation/details-ville", // On ajoute l'url absolue en commençant par la racine
                type: 'get',
                data: {
                    id: $(this).val(),
                },
                success: function(data){
                    // On initialise la selection du département
                    select_ville.html('');
                    select_ville.append("<option value='' selected>--- Selectionnez une ville ---</option>");

                    // On initialise la selection de la commune
                    select_commune.html('');
                    select_commune.append("<option value='' selected>--- Selectionnez une commune ---</option>");

                    $.each(data.data, function(key, value){
                        select_ville.append("<option value='" + value.id + "' >" + value.libelle + "</option>");
                    });
                },
            });


        });

        // Traitement AJAX de la commune
        $(select_ville).change(function(){

            // On utilise ajax pour récupérer les villes
            $.ajax({
                url: "/localisation/details-commune", // On ajoute l'url absolue en commençant par la racine
                type: 'get',
                data: {
                    id: $(this).val(),
                },
                success: function(data){
                    // On initialise la selection du département
                    select_commune.html('');
                    select_commune.append("<option value='' selected>--- Selectionnez une commune ---</option>");

                    $.each(data.data, function(key, value){
                        select_commune.append("<option value='" + value.id + "' >" + value.libelle + "</option>");
                    });
                },
            });

        });


// ******************* GESTION DES AFFICHAGES DU CHAMP DATE DE NAISSANCE *****************************
    var label_naissance = $('#label_naissance');
    var label_naissance_times = $('#label_naissance_times');
    var label_naissance_plus = $('#label_naissance_plus');
    var naissance_btn_ajouter = $('#naissance_btn_ajouter');
    var lieu_naissance = $('#lieu_naissance');
    var date_de_naissance_Modal = $('#date_de_naissance_Modal');
    var naissance_btn_fermer = $('#naissance_btn_fermer');

    label_naissance_times.click(function(){
        label_naissance.val('');
        lieu_naissance.val('');
    });

    naissance_btn_ajouter.click(function(e){
        e.preventDefault();
        if(select_commune.val()){
            label_naissance.val($('select[name=select_commune] option:selected').text());
            lieu_naissance.val(select_commune.val());
            date_de_naissance_Modal.hide('slow');
            naissance_btn_fermer.trigger('click');
        }
    });


// ******************* GESTION AJAX DE L'AJOUT D'UNE COOPERATIVE *****************************

    var cooperative_a_ajouter = $('#cooperative_a_ajouter');
    var cooperative_a_fermer = $('#cooperative_a_fermer');
    var cooperative_a_annuler = $('#cooperative_a_annuler');
    var cooperative_l_fermer = $('#cooperative_l_fermer');

    var label_cooperative_times = $('#label_cooperative_times');
    var cooperative = $('#cooperative');
    var cooperative_texte = $('#cooperative_texte');

        // On vide les champs
        label_cooperative_times.click(function(){
            cooperative.val("");
            cooperative_texte.val("");
        });

        // Traitement AJAX
        cooperative_a_ajouter.click(function(e){
            e.preventDefault(); // On annule l'envoi du formulaire

            // On utilise ajax pour récupérer les régions
            $.ajax({
                url: "/vieprofessionnelle/ajouter-cooperative", // On ajoute l'url absolue en commençant par la racine
                type: 'post',
                data: {
                    id_json: $('#id_json').val(),
                    nom_cooperative: $('#nom_cooperative').val(),
                    presidente: $('#presidente').val(),
                    contact_presidente: $('#contact_presidente').val(),
                    speculation_agricole: $('#speculation_agricole').val(),
                    superficie_en_culture: $('#superficie_en_culture').val(),
                    superficie_en_production: $('#superficie_en_production').val(),
                    gps_longitude: $('#gps_longitude').val(),
                    gps_latitude: $('#gps_latitude').val(),
                    dateenre: $('#dateenre').val(),
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                },
                success: function(data){

                    // On remplit les champs
                    cooperative.val(data.data.id);
                    cooperative_texte.val(data.data.cooperative);

                    // Affichage du message
                    alert(data.data.message);

                    // Gestion des fermetures des boutons
                    cooperative_a_annuler.trigger('click'); // On initialise les champs du modal en cours
                    cooperative_a_fermer.trigger('click'); // On ferme le modal en cours
                    cooperative_l_fermer.trigger('click'); // On ferme le modal de la recherche
                },
                statusCode: {
                    404: function(data){
                            alert('Veuillez renseigner les champs SVP.');
                         },
                    400: function(data){
                            alert('Cette coopérative existe déjà.');
                         },
                },
            });


        });

    // Partie 2

    var liens = $("#table_recherche_cooperative tbody td a");
        liens.each(function(){

            $(this).click(function(){
                // On remplit les champs
                 cooperative.val($(this).attr('value')); // On récupère le id du Secteur Agricole
                 cooperative_texte.val($(this).text()); // On affiche le nom de la coopérative
                 cooperative_l_fermer.trigger('click'); // On ferme le modal de la recherche
            });

        });





// ****************************************************************************

});