#!/bin/bash
# Refresh repo copy from the working folder using the approved layout
set -e; S=/mnt/project-files/1808-eruption; N=$S/notes; R=${1:-/mnt/project-files/1808-eruption-repo}
cd $R
cp $S/why_unidentified.md findings/; cp $S/interim_summary.md findings/archive/; cp $S/source_register.md sources/register.md
declare -A M=(
[colombia_caldas]="caldas.md caldas_portraits_public_domain_2026-11-27.md caldas_letters_round2.md caldas_roulin_golovnin_pass2.md caldas_correspondents_pass3.md restrepo_date_round3.md cotopaxi_1808_round3.md"
[peru_south]="unanue_south.md andes_south_catalogues_round3.md travel_southcone_pass3.md"
[mexico_caribbean_spain]="spanish_north.md mexico_centralam_round3.md central_america_round4.md caribbean_papers_round3.md gazeta_mexico_reading_passes gazeta_madrid_reading_passes mallorca_reading_passes diario_mexico_reading_passes caracas_reading_passes"
[portuguese_world]="lusophone.md iberian_fulltext_pass2.md iberian_logs_round2.md ramoncita_bvd_2026-11-02.md"
[asia_pacific_arabic]="asian_arabic_round4.md pacific_china_pass3.md insular_asia_pass3.md indonesia_pass2.md maritime_indopacific.md asiatic_annual_register_scan.md japanese_red_skies_literature_2026-10-26.md moluccas_newbritain_records_2026-10-26.md newbritain_banda_halmahera_records_2026-10-26.md wichmann_catalogue_2026-10-26.md chinese_gazetteers_reaches_2026-10-27.md dutch_colonial_archives_1808-10_2026-10-27.md tonga_tahiti_hawaii_1808-10_2026-10-27.md dai_nam_thuc_luc_1808-10_2026-10-28.md"
[north_america]="hbc_york_factory_journals.md hbc_churchill_journals.md hbc_moose_journals.md hbc_edmonton_journals.md nw_america_round2.md north_pacific_round2.md daily_journals_round2.md"
[ship_logs]="wexford_journal_feb-jul1808.md wexford_journal_aug1808-mar1809.md wexford_journal_nov-dec1808.md royal_george_canton_jul1808-apr1809.md indian_atlantic_pass3.md american_logbooks_2026-10-27.md tna_record_copying_test_cornwallis_2026-10-28.md fleet_log_inventory_2026-11-02.md"
[europe_press]="euro_journals_round3.md newspapers_1809_round2.md nonIberian_fulltext_pass2.md dutch_papers_round2.md free_sources_round5.md newspaper_downloads_round5.md eyewitness_books_pass2.md retrospective_round2.md dutch_papers_newterms_2026-10-21.md"
[science_alternatives]="scientific_data_round6.md nonvolcanic_alternatives.md gvp_1806_1811.md literature.md antarctic_sulfate_map_2026-10-26.md krakatoa_report_historical_twilights_2026-10-26.md lunar_eclipses_1808-09_2026-10-26.md coral_treering_enso_1809_2026-10-27.md tephra_databases_1805-1812_2026-10-27.md bipolar_sulfate_lag_2026-10-27.md coral_footprint_1809-12_2026-10-28.md deposition_ratio_validation_2026-10-28.md tibet_himalaya_records_2026-10-28.md"
[candidates]="trace_element_lookup_2026-11-02.md gvp_candidates_and_volcanocafe_2026-10-22.md glass_comparison_2026-10-22.md glass_candidates_compilation_2026-10-26.md glass_candidates_compositions.md glass_ice_1809_compositions.md long_island_post_tibito_2026-10-26.md candidate_profiles_dakataua_sbanda_2026-10-26.md candidate_priority_list_2026-10-26.md cabalian_parish_records_familysearch_2026-10-28.md bohol_burial_entries_by_image_2026-10-28.md existing_cores_near_candidates_2026-10-28.md"
[melanesia_oral]="oral_history_melanesia.md blong_time_of_darkness.md"
[method]="hosting_licence_audit_2026-11-04.md language_corrections_log.md findings_table_check_2026-11-04.md october_leads_audit_T16_2026-11-02.md evidence_that_would_settle_it_2026-11-02.md free_checks_T5-T10_2026-11-02.md eruption_clue_search_terms.md novelty_check_round3.md downloads_2026-10-16_findings.md eruption_markers_knowledge_base.md easy_leads_2026-10-22.md papers_downloaded_2026-10-22.md script_downloads_read_2026-10-27.md creative_next_steps_2026-10-28.md wide_source_search_2026-11-04.md new_scholarship_check_2026-11-12.md grokipedia_audit_2026-11-12.md"
[../access]="eic_access.md")
for d in "${!M[@]}"; do mkdir -p "strands/$d"; for f in ${M[$d]}; do cp -r "$N/$f" "strands/$d/"; done; done
# One-page summary per strand folder (T29, 4 Nov 2026): master copies live in $S/strand_readmes/<folder>.md
for f in $S/strand_readmes/*.md; do d=$(basename "$f" .md); mkdir -p "strands/$d"; cp "$f" "strands/$d/README.md"; done
cp $S/newspaper_access_guide.md $S/download_links.md $S/unavailable_sources.md $S/open_tasks.md $S/catalogue_sweep_*.md access/
mkdir -p figures; cp $S/figures/* figures/; find $S/data -maxdepth 1 -type f -exec cp {} data/ \;; mkdir -p data/cc-by-sa; cp $S/data/cc-by-sa/* data/cc-by-sa/; cp $S/scripts/fetch_newspapers.py $S/scripts/README.md scripts/; cp -r $S/scripts/fleet_map_2026-11-02 $S/scripts/trace_lookup_2026-11-02 $S/scripts/round6 $S/scripts/antarctic_sulfate_2026-10-26 $S/scripts/creative_next_steps_2026-10-28 $S/scripts/dai_nam_thuc_luc_2026-10-28 $S/scripts/deposition_validation_2026-10-28 $S/scripts/coral_footprint_2026-10-28 $S/scripts/tibet_icecores_2026-10-28 $S/scripts/glass_vanuatu_solomons_2026-11-02 $S/scripts/bipolar_lag_2026-10-27 $S/scripts/coral_enso_2026-10-27 $S/scripts/reaches_2026-10-27 $S/scripts/detection_floor_2026-11-04 $S/scripts/related_mysteries_2026-11-04 scripts/; cp $S/scripts/gvp_candidates.py $S/scripts/glass_similarity_2026-10-26.py $S/scripts/score_georoc_2026-10-26.py $S/scripts/score_gill_ecl_2026-10-26.py $S/scripts/sync_repo_copy.sh $S/scripts/fetch_unavailable.py $S/scripts/add_frontmatter.py $S/scripts/fetch_bl_iiif.py $S/scripts/archive_grokipedia.sh scripts/
# FamilySearch scripts (fs_film_fetch.py, fs_diag*.py) stay on the Mac and are never synced (licence audit 4 Nov 2026).
# Community layer (README, CONTRIBUTING, .github/, community/ ...) lives only in the repo copy; nothing above touches it.
# Re-stamp AI-provenance front matter on the freshly copied notes (idempotent; human checks come from community/verification_overrides.csv)
python3 $R/scripts/add_frontmatter.py $R
for f in $(ls $N); do grep -qw "$f" <<< "${M[*]}" || echo "UNMAPPED notes/$f"; done
for f in $(ls $S/data); do :; done
