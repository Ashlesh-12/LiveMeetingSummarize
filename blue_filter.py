<!DOCTYPE html>
<!-- saved from url=(0053)https://github.com/SharmilaShroff/image-processing.py -->
<html lang="en" data-color-mode="auto" data-light-theme="light" data-dark-theme="dark" data-a11y-animated-images="system" data-a11y-link-underlines="true" class="js-focus-visible" data-js-focus-visible="" data-turbo-loaded=""><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><style type="text/css">.turbo-progress-bar {
  position: fixed;
  display: block;
  top: 0;
  left: 0;
  height: 3px;
  background: #0076ff;
  z-index: 2147483647;
  transition:
    width 300ms ease-out,
    opacity 150ms 150ms ease-in;
  transform: translate3d(0, 0, 0);
}
</style><style>
:root {
  --fontStack-monospace: "Monaspace Neon", ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace !important;
}
</style>




  
    
  <link rel="dns-prefetch" href="https://github.githubassets.com/">
  <link rel="dns-prefetch" href="https://avatars.githubusercontent.com/">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com/">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">
  <link rel="preconnect" href="https://github.githubassets.com/" crossorigin="">
  <link rel="preconnect" href="https://avatars.githubusercontent.com/">

  

  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./blue_filter_files/light-dac525bbd821.css"><link crossorigin="anonymous" media="all" rel="stylesheet" href="./blue_filter_files/dark-784387e86ac0.css"><link data-color-theme="light_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_high_contrast-56ccf4057897.css"><link data-color-theme="light_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_colorblind-0e24752a7d2b.css"><link data-color-theme="light_colorblind_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_colorblind_high_contrast-412af2517363.css"><link data-color-theme="light_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_tritanopia-6186e83663dc.css"><link data-color-theme="light_tritanopia_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_tritanopia_high_contrast-9d33c7aea2e7.css"><link data-color-theme="dark_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_high_contrast-79bd5fd84a86.css"><link data-color-theme="dark_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_colorblind-75db11311555.css"><link data-color-theme="dark_colorblind_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_colorblind_high_contrast-f2c1045899a2.css"><link data-color-theme="dark_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_tritanopia-f46d293c6ff3.css"><link data-color-theme="dark_tritanopia_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_tritanopia_high_contrast-e4b5684db29d.css"><link data-color-theme="dark_dimmed" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_dimmed-72c58078e707.css"><link data-color-theme="dark_dimmed_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_dimmed_high_contrast-956cb5dfcb85.css">

  <style type="text/css">
    :root {
      --tab-size-preference: 4;
    }

    pre, code {
      tab-size: var(--tab-size-preference);
    }
  </style>

    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./blue_filter_files/primer-primitives-c37d781e2da5.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./blue_filter_files/primer-8bf3328b2828.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./blue_filter_files/global-df4c2156a48b.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./blue_filter_files/github-f7230554fa20.css">
  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./blue_filter_files/repository-5d735668c600.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./blue_filter_files/code-9c9b8dc61e74.css">

  

  <script type="application/json" id="client-env">{"locale":"en","featureFlags":["a11y_status_checks_ruleset","actions_custom_images_public_preview_visibility","actions_custom_images_storage_billing_ui_visibility","actions_enable_snapshot_keyword","actions_image_version_event","agent_session_retry_fetch_capi_on_401","allow_react_navs_in_turbo","alternate_user_config_repo","api_insights_show_missing_data_banner","arianotify_comprehensive_migration","arianotify_partial_migration","billing_hard_budget_limits_for_licenses","billing_ui_budget_pagination_enabled","client_version_header","codespaces_prebuild_region_target_update","coding_agent_model_selection","contentful_lp_footnotes","copilot_agent_cli_public_preview","copilot_agent_sessions_alive_updates","copilot_agent_task_list_v2","copilot_agent_tasks_btn_code_nav","copilot_agent_tasks_btn_code_view","copilot_agent_tasks_btn_code_view_lines","copilot_agent_tasks_btn_repo","copilot_agents_blankslate_mem_requests","copilot_api_agentic_issue_marshal_yaml","copilot_api_draft_issue_reference_with_project_id","copilot_api_github_draft_update_issue_skill","copilot_capi_error_response_telemetry","copilot_chat_agents_empty_state","copilot_chat_attach_multiple_images","copilot_chat_clear_model_selection_for_default_change","copilot_chat_disable_model_picker_while_streaming","copilot_chat_file_redirect","copilot_chat_input_commands","copilot_chat_opening_thread_switch","copilot_chat_reduce_quota_checks","copilot_chat_search_bar_redirect","copilot_chat_selection_attachments","copilot_chat_vision_in_claude","copilot_chat_vision_preview_gate","copilot_coding_agent_task_response","copilot_custom_copilots","copilot_custom_copilots_feature_preview","copilot_duplicate_thread","copilot_extensions_hide_in_dotcom_chat","copilot_extensions_removal_on_marketplace","copilot_features_raycast_logo","copilot_file_block_ref_matching","copilot_ftp_hyperspace_upgrade_prompt","copilot_icebreakers_experiment_dashboard","copilot_icebreakers_experiment_hyperspace","copilot_immersive_generate_thread_name_async","copilot_immersive_job_result_preview","copilot_immersive_structured_model_picker","copilot_immersive_task_hyperlinking","copilot_immersive_task_within_chat_thread","copilot_issue_list_show_more","copilot_org_policy_page_focus_mode","copilot_pipes_code_nodes","copilot_pipes_github_graphql_nodes","copilot_premium_request_quotas","copilot_redirect_header_button_to_agents","copilot_security_alert_assignee_options","copilot_share_active_subthread","copilot_spaces_ga","copilot_spaces_individual_policies_ga","copilot_spaces_public_access_to_user_owned_spaces","copilot_spaces_read_access_to_user_owned_spaces","copilot_spaces_report_abuse","copilot_spark_empty_state","copilot_spark_handle_nil_friendly_name","copilot_spark_loading_webgl","copilot_stable_conversation_view","copilot_swe_agent_progress_commands","copilot_swe_agent_use_subagents","copilot_unconfigured_is_inherited","dashboard_indexeddb_caching","dashboard_universe_2025","dashboard_universe_2025_feedback_dialog","direct_to_salesforce","dom_node_counts","dotcom_chat_client_side_skills","enterprise_ai_controls","failbot_report_error_react_apps_on_page","fetch_graphql_improved_error_serialization","fgpat_permissions_selector_redesign","flex_cta_groups_mvp","global_nav_react_edit_status_dialog","global_nav_react_feature_preview","global_nav_react_teams_settings_page","global_nav_react_top_repos_api_caching","hide_groups_list_for_few_groups","hyperspace_2025_logged_out_batch_1","initial_per_page_pagination_updates","issue_fields_global_search","issue_fields_report_usage","issue_fields_timeline_events","issues_cca_assign_actor_with_agent","issues_expanded_file_types","issues_lazy_load_comment_box_suggestions","issues_react_bots_timeline_pagination","issues_react_chrome_container_query_fix","issues_react_client_side_caching_analytics","issues_react_include_bots_in_pickers","issues_react_prohibit_title_fallback","issues_react_ui_feedback","issues_react_use_turbo_for_cross_repo_navigation","issues_report_sidebar_interactions","lifecycle_label_name_updates","link_contact_sales_swp_marketo","loops_service_graphql_execution","marketing_pages_search_explore_provider","memex_default_issue_create_repository","memex_grouped_by_edit_route","memex_mwl_filter_field_delimiter","memex_roadmap_drag_style","mission_control_use_body_html","new_traffic_page_banner","open_agent_session_in_vscode_insiders","open_agent_session_in_vscode_stable","pr_react_progressive_queue","pr_sfv_new_diff_fetch","projects_assignee_max_limit","react_compiler_commits","react_compiler_diff_lines","react_compiler_markdown_editor","react_compiler_prs_hooks","react_compiler_prs_ui","react_compiler_pull_requests","react_custom_partial_router","react_fetch_graphql_ignore_expected_errors","render_user_display_name","repo_traffic_job","repos_insights_remove_new_url","repository_suggester_elastic_search","ruleset_deletion_confirmation","sample_network_conn_type","scheduled_reminders_updated_limits","site_calculator_actions_2025","site_features_copilot_universe","site_homepage_collaborate_video","site_homepage_contentful","site_homepage_eyebrow_banner","site_homepage_universe_animations","site_msbuild_webgl_hero","spark_prompt_secret_scanning","swe_agent_member_requests","swe_agent_member_requests_agent_panel","viewscreen_sandbox","webp_support","workbench_store_readonly"],"login":"SharmilaShroff","copilotApiOverrideUrl":"https://api.individual.githubcopilot.com"}</script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/wp-runtime-1f8c6ba049f5.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/913-ca2305638c53.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/6488-de87864e6818.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/environment-b3d48626cc6e.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/69676-3e4d0020216a.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/43784-4652ae97a661.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/4712-6fc930a63a4b.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/81028-5b8c5e07a4fa.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/97292-9890ce009c4e.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/91853-2ed22fb46437.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/78143-31968346cf4c.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/52430-2f44a4a36933.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/github-elements-8b5d9b8ccf1f.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/element-registry-b55e55b2dbe9.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/react-lib-760965ba27bb.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/react-core-c947eff3bbc1.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/28546-ee41c9313871.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/17688-a9e16fb5ed13.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/2869-a4ba8f17edb3.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/70191-5122bf27bf3e.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/7332-5ea4ccf72018.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/3561-5983d983527e.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/24077-adc459723b71.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/51519-d3c416bc1076.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/27376-9825e0a74a24.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/96384-750ef5263abe.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/19718-676a65610616.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/behaviors-7b6a98bc4afa.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/48011-1f20a5c80dd7.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/notifications-global-54f7f2032e0d.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/39713-8508e9483898.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/45688-b093405a7bf6.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/90787-3d665c8ee86e.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/5903-3cd556b5e9d3.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/codespaces-5b6c0f0d4ee9.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/23387-1b12da426b92.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/72568-b0582cf2bbee.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/13974-18aebd0d0d21.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/14155-c583ca76c604.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/repositories-37aa1111d71f.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/31615-236504c8966f.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/code-menu-fa1d4025778b.js.download" defer="defer"></script>
  
  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./blue_filter_files/primer-react.47239ec6cbe68138fe4c.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./blue_filter_files/notifications-subscriptions-menu.933100a30c03fd4e8ae4.module.css">


  <title>SharmilaShroff/image-processing.py: A Python script that loads an image, applies a strong box blur using Pillow (PIL), and displays the blurred output with Matplotlib.</title>



  <meta name="route-pattern" content="/:user_id/:repository" data-turbo-transient="">
  <meta name="route-controller" content="files" data-turbo-transient="">
  <meta name="route-action" content="disambiguate" data-turbo-transient="">
  <meta name="fetch-nonce" content="v2:2b815f31-74b1-a9f7-c69b-a73f6467a217">

    
  <meta name="current-catalog-service-hash" content="f3abb0cc802f3d7b95fc8762b94bdcb13bf39634c40c357301c4aa1d67a256fb">


  <meta name="request-id" content="CE1F:99196:279A32:2B14D1:695BCE6F" data-turbo-transient="true"><meta name="html-safe-nonce" content="f83104944c00832e008ed2d2f8ac1e59306ac71e7346bdd02cd9b7ef25e21bac" data-turbo-transient="true"><meta name="visitor-payload" content="eyJyZWZlcnJlciI6Imh0dHBzOi8vZ2l0aHViLmNvbS8iLCJyZXF1ZXN0X2lkIjoiQ0UxRjo5OTE5NjoyNzlBMzI6MkIxNEQxOjY5NUJDRTZGIiwidmlzaXRvcl9pZCI6IjU5OTM0NDczNzY2MjM5MTM2ODYiLCJyZWdpb25fZWRnZSI6ImNlbnRyYWxpbmRpYSIsInJlZ2lvbl9yZW5kZXIiOiJpYWQifQ==" data-turbo-transient="true"><meta name="visitor-hmac" content="9dbcf8eb12a9e60e0a08afdb65eed7de3cb12a014216712c839bbbd8c1cb65d1" data-turbo-transient="true">


    <meta name="hovercard-subject-tag" content="repository:1098386497" data-turbo-transient="">


  <meta name="github-keyboard-shortcuts" content="repository,copilot" data-turbo-transient="true">
  

  <meta name="selected-link" value="repo_source" data-turbo-transient="">
  <link rel="assets" href="https://github.githubassets.com/">

    <meta name="google-site-verification" content="Apib7-x98H0j5cPqHWwSMm6dNU4GmODRoqxLiDzdx9I">

<meta name="octolytics-url" content="https://collector.github.com/github/collect"><meta name="octolytics-actor-id" content="190357636"><meta name="octolytics-actor-login" content="SharmilaShroff"><meta name="octolytics-actor-hash" content="4264ad64b97735e2607c131bb5394c059bcc2a35f9ee8c53150e9955dd28a908">

  <meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;" data-turbo-transient="true">

  




    <meta name="user-login" content="SharmilaShroff">

  <link rel="sudo-modal" href="https://github.com/sessions/sudo_modal">

    <meta name="viewport" content="width=device-width">

    

      <meta name="description" content="A Python script that loads an image, applies a strong box blur using Pillow (PIL), and displays the blurred output with Matplotlib. - SharmilaShroff/image-processing.py">

      <link rel="search" type="application/opensearchdescription+xml" href="https://github.com/opensearch.xml" title="GitHub">

    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <meta property="fb:app_id" content="1401488693436528">
    <meta name="apple-itunes-app" content="app-id=1477376905, app-argument=https://github.com/SharmilaShroff/image-processing.py">

      <meta name="twitter:image" content="https://opengraph.githubassets.com/6f72a9969c7d96cdc3b03dbbf6558ddf1f35de9f07f961bf53b9c905ad69cd18/SharmilaShroff/image-processing.py"><meta name="twitter:site" content="@github"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="SharmilaShroff/image-processing.py: A Python script that loads an image, applies a strong box blur using Pillow (PIL), and displays the blurred output with Matplotlib."><meta name="twitter:description" content="A Python script that loads an image, applies a strong box blur using Pillow (PIL), and displays the blurred output with Matplotlib. - SharmilaShroff/image-processing.py">
  <meta property="og:image" content="https://opengraph.githubassets.com/6f72a9969c7d96cdc3b03dbbf6558ddf1f35de9f07f961bf53b9c905ad69cd18/SharmilaShroff/image-processing.py"><meta property="og:image:alt" content="A Python script that loads an image, applies a strong box blur using Pillow (PIL), and displays the blurred output with Matplotlib. - SharmilaShroff/image-processing.py"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="600"><meta property="og:site_name" content="GitHub"><meta property="og:type" content="object"><meta property="og:title" content="SharmilaShroff/image-processing.py: A Python script that loads an image, applies a strong box blur using Pillow (PIL), and displays the blurred output with Matplotlib."><meta property="og:url" content="https://github.com/SharmilaShroff/image-processing.py"><meta property="og:description" content="A Python script that loads an image, applies a strong box blur using Pillow (PIL), and displays the blurred output with Matplotlib. - SharmilaShroff/image-processing.py">
  


      <link rel="shared-web-socket" href="wss://alive.github.com/_sockets/u/190357636/ws?session=eyJ2IjoiVjMiLCJ1IjoxOTAzNTc2MzYsInMiOjE4NjY5MDA3MjcsImMiOjIwMDQ1NzIzOSwidCI6MTc2NzYyNDMwNH0=--b5b59212ca75c0178a45f87314cb1b2fcb3a21113a6c389e66336a13fcd89154" data-refresh-url="/_alive" data-session-id="40bb50da0476e06b6c389559d8a7bce1929a4bc627a00692387341e428704885">
      <link rel="shared-web-socket-src" href="https://github.com/assets-cdn/worker/socket-worker-2a038060e454.js">


      <meta name="hostname" content="github.com">


      <meta name="keyboard-shortcuts-preference" content="all">
      <meta name="hovercards-preference" content="true">
      <meta name="announcement-preference-hovercard" content="true">

        <meta name="expected-hostname" content="github.com">


  <meta http-equiv="x-pjax-version" content="a329ad62eb66ff4e917800ab16c5532a96a3e9c10fec4eb2fb06754df3989354" data-turbo-track="reload">
  <meta http-equiv="x-pjax-csp-version" content="21a43568025709b66240454fc92d4f09335a96863f8ab1c46b4a07f6a5b67102" data-turbo-track="reload">
  <meta http-equiv="x-pjax-css-version" content="03da391a01750e54015d0ebd9e7e968879f966ef76d8a697be72ccbc12abac55" data-turbo-track="reload">
  <meta http-equiv="x-pjax-js-version" content="4284fcdae2467c0488f403003014c66ea2c39f6cffc1823a99c0e82c51a1212d" data-turbo-track="reload">

  <meta name="turbo-cache-control" content="no-preview" data-turbo-transient="">

      <meta data-hydrostats="publish">
  <meta name="go-import" content="github.com/SharmilaShroff/image-processing.py git https://github.com/SharmilaShroff/image-processing.py.git">

  <meta name="octolytics-dimension-user_id" content="190357636"><meta name="octolytics-dimension-user_login" content="SharmilaShroff"><meta name="octolytics-dimension-repository_id" content="1098386497"><meta name="octolytics-dimension-repository_nwo" content="SharmilaShroff/image-processing.py"><meta name="octolytics-dimension-repository_public" content="true"><meta name="octolytics-dimension-repository_is_fork" content="false"><meta name="octolytics-dimension-repository_network_root_id" content="1098386497"><meta name="octolytics-dimension-repository_network_root_nwo" content="SharmilaShroff/image-processing.py">



      <link rel="canonical" href="https://github.com/SharmilaShroff/image-processing.py" data-turbo-transient="">


    <meta name="turbo-body-classes" content="logged-in env-production page-responsive">
  <meta name="disable-turbo" content="false">


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <meta name="release" content="1a6cdce5a553c86c60bc512bedc6b4dc1cc41675">
  <meta name="ui-target" content="full">

  <link rel="mask-icon" href="https://github.githubassets.com/assets/pinned-octocat-093da3e6fa40.svg" color="#000000">
  <link rel="alternate icon" class="js-site-favicon" type="image/png" href="https://github.githubassets.com/favicons/favicon.png">
  <link rel="icon" class="js-site-favicon" type="image/svg+xml" href="https://github.githubassets.com/favicons/favicon.svg" data-base-href="https://github.githubassets.com/favicons/favicon">

<meta name="theme-color" content="#1e2327">
<meta name="color-scheme" content="light dark">

  <meta name="msapplication-TileImage" content="/windows-tile.png">
  <meta name="msapplication-TileColor" content="#ffffff">

  <link rel="manifest" href="https://github.com/manifest.json" crossorigin="use-credentials">

  <link rel="stylesheet" type="text/css" href="./blue_filter_files/14814.29aaeaafa90f007c6f61.module.css" crossorigin="anonymous"><link rel="stylesheet" type="text/css" href="./blue_filter_files/24291.933100a30c03fd4e8ae4.module.css" crossorigin="anonymous"><link rel="stylesheet" type="text/css" href="./blue_filter_files/47657.b14b6fddffe5b4a1fb97.module.css" crossorigin="anonymous"><style data-styled="active" data-styled-version="5.3.11"></style><link rel="stylesheet" type="text/css" href="./blue_filter_files/86427.a752e1d5a8c3aad1a210.module.css" crossorigin="anonymous"><link rel="stylesheet" type="text/css" href="./blue_filter_files/1650.9d926f69ee309a45d0df.module.css" crossorigin="anonymous"><link rel="stylesheet" type="text/css" href="./blue_filter_files/16702.30736d4aa7b2b246dd6f.module.css" crossorigin="anonymous"><link rel="stylesheet" type="text/css" href="./blue_filter_files/71699.f4d276768bcd7cf634b3.module.css" crossorigin="anonymous"><link rel="stylesheet" type="text/css" href="./blue_filter_files/6873.44b521786393825e5c12.module.css" crossorigin="anonymous"><style id="ms-consent-banner-main-styles">.w8hcgFksdo30C8w-bygqu{color:#000}.ydkKdaztSS0AeHWIeIHsQ a{color:#0067B8}.erL690_8JwUW-R4bJRcfl{background-color:#EBEBEB;border:none;color:#000}.erL690_8JwUW-R4bJRcfl:enabled:hover{color:#000;background-color:#DBDBDB;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:none}.erL690_8JwUW-R4bJRcfl:enabled:focus{background-color:#DBDBDB;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:2px solid #000}.erL690_8JwUW-R4bJRcfl:disabled{opacity:1;color:rgba(0,0,0,0.2);background-color:rgba(0,0,0,0.2);border:none}._1zNQOqxpBFSokeCLGi_hGr{border:none;background-color:#0067B8;color:#fff}._1zNQOqxpBFSokeCLGi_hGr:enabled:hover{color:#fff;background-color:#0067B8;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:none}._1zNQOqxpBFSokeCLGi_hGr:enabled:focus{background-color:#0067B8;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:2px solid #000}._1zNQOqxpBFSokeCLGi_hGr:disabled{opacity:1;color:rgba(0,0,0,0.2);background-color:rgba(0,120,215,0.2);border:none}._23tra1HsiiP6cT-Cka-ycB{position:relative;display:flex;z-index:9999;width:100%;background-color:#F2F2F2;justify-content:space-between;text-align:left}div[dir="rtl"]._23tra1HsiiP6cT-Cka-ycB{text-align:right}._1Upc2NjY8AlDn177YoVj0y{margin:0;padding-left:5%;padding-top:8px;padding-bottom:8px}div[dir="rtl"] ._1Upc2NjY8AlDn177YoVj0y{margin:0;padding:8px 5% 8px 0;float:none}._23tra1HsiiP6cT-Cka-ycB svg{fill:none;max-width:none;max-height:none}._1V_hlU-7jdtPiooHMu89BB{display:table-cell;padding:12px;width:24px;height:24px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:24px;line-height:0}.f6QKJD7fhSbnJLarTL-W-{display:table-cell;vertical-align:middle;padding:0;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:13px;line-height:16px}.f6QKJD7fhSbnJLarTL-W- a{text-decoration:underline}._2j0fmugLb1FgYz6KPuB91w{display:inline-block;margin-left:5%;margin-right:5%;min-width:40%;min-width:calc((150px + 3 * 4px) * 2 + 150px);min-width:-webkit-fit-content;min-width:-moz-fit-content;min-width:fit-content;align-self:center;position:relative}._1XuCi2WhiqeWRUVp3pnFG3{margin:4px;padding:5px;min-width:150px;min-height:36px;vertical-align:top;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._1XuCi2WhiqeWRUVp3pnFG3:focus{box-sizing:border-box}._1XuCi2WhiqeWRUVp3pnFG3:disabled{cursor:not-allowed}._2bvsb3ubApyZ0UGoQA9O9T{display:block;position:fixed;z-index:10000;top:0;left:0;width:100%;height:100%;background-color:rgba(255,255,255,0.6);overflow:auto;text-align:left}div[dir="rtl"]._2bvsb3ubApyZ0UGoQA9O9T{text-align:right}div[dir="rtl"] ._2bvsb3ubApyZ0UGoQA9O9T{left:auto;right:0}.AFsJE948muYyzCMktdzuk{position:relative;top:8%;margin-bottom:40px;margin-left:auto;margin-right:auto;box-sizing:border-box;width:640px;background-color:#fff;border:1px solid #0067B8}._3kWyBRbW_dgnMiEyx06Fu4{float:right;z-index:1;margin:2px;padding:12px;border:none;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:13px;line-height:13px;display:flex;align-items:center;text-align:center;color:#666;background-color:#fff}div[dir="rtl"] ._3kWyBRbW_dgnMiEyx06Fu4{margin:2px;padding:12px;float:left}.uCYvKvHXrhjNgflv1VqdD{position:static;margin-top:36px;margin-left:36px;margin-right:36px}._17pX1m9O_W--iZbDt3Ta5r{margin-top:0;margin-bottom:12px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:20px;line-height:24px;text-transform:none}._1kBkHQ1V1wu3kl-YcLgUr6{height:446px;overflow:auto}._20_nXDf6uFs9Q6wxRXG-I-{margin-top:0;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px}._20_nXDf6uFs9Q6wxRXG-I- a{text-decoration:underline}dl._2a0NH_GDQEQe5Ynfo7suVH{margin-top:36px;margin-bottom:0;padding:0;list-style:none;text-transform:none}dt._3j_LCPv7fyXv3A8FIXVwZ4{margin-top:20px;float:none;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:18px;line-height:24px;list-style:none}.k-vxTGFbdq1aOZB2HHpjh{margin:0;padding:0;border:none}._2Bucyy75c_ogoU1g-liB5R{margin:0;padding:0;border-bottom:none;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:18px;line-height:24px;text-transform:none}._63gwfzV8dclrsl2cfd90r{display:inline-block;margin-top:0;margin-bottom:13px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px}._1l8wM_4mRYGz3Iu7l3BZR7{display:block}._2UE03QS02aZGkslegN_F-i{display:inline-block;position:relative;left:5px;margin-bottom:13px;margin-right:34px;padding:3px}div[dir="rtl"] ._2UE03QS02aZGkslegN_F-i{margin:0 0 13px 34px;padding:3px;float:none}div[dir="rtl"] ._2UE03QS02aZGkslegN_F-i{left:auto;right:5px}._23tra1HsiiP6cT-Cka-ycB *::before,._2bvsb3ubApyZ0UGoQA9O9T *::before,._23tra1HsiiP6cT-Cka-ycB *::after,._2bvsb3ubApyZ0UGoQA9O9T *::after{box-sizing:inherit}._1HSFn0HzGo6w4ADApV8-c4{outline:2px solid rgba(0,0,0,0.8)}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2{display:inline-block;position:relative;margin-top:0;margin-left:0;margin-right:0;height:0;width:0;border-radius:0;cursor:pointer;outline:none;box-sizing:border-box;-webkit-appearance:none;-moz-appearance:none;appearance:none}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2+label::before{display:block;position:absolute;top:5px;left:3px;height:19px;width:19px;content:"";border-radius:50%;border:1px solid #000;background-color:#fff}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2+label::before{left:auto;right:3px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::before{border:1px solid #0067B8}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:rgba(0,0,0,0.8)}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::before{border:1px solid #0067B8}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:#000}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked+label::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:#000}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked+label::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled+label{cursor:not-allowed}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled+label::before{border:1px solid rgba(0,0,0,0.2);background-color:rgba(0,0,0,0.2)}._3RJzeL3l9Rl_lAQEm6VwdX{display:block;position:static;float:right;margin-top:0;margin-bottom:0;margin-left:19px;margin-right:0;padding-top:0;padding-bottom:0;padding-left:8px;padding-right:0;width:80%;width:calc(100% - 19px);font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-transform:none;cursor:pointer;box-sizing:border-box}div[dir="rtl"] ._3RJzeL3l9Rl_lAQEm6VwdX{margin:0 19px 0 0;padding:0 8px 0 0;float:left}.nohp3sIG12ZBhzcMnPala{margin-top:20px;margin-bottom:48px}._2uhaEsmeotZ3P-M0AXo2kF{padding:0;width:278px;height:36px;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._2uhaEsmeotZ3P-M0AXo2kF:focus{box-sizing:border-box}._2uhaEsmeotZ3P-M0AXo2kF:disabled{cursor:not-allowed}._3tOu1FJ59c_xz_PmI1lKV5{float:right;padding:0;width:278px;height:36px;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._3tOu1FJ59c_xz_PmI1lKV5:focus{box-sizing:border-box}._3tOu1FJ59c_xz_PmI1lKV5:disabled{cursor:not-allowed}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0;padding:0;float:left}@media only screen and (max-width: 768px){._2j0fmugLb1FgYz6KPuB91w,._1Upc2NjY8AlDn177YoVj0y{padding-top:8px;padding-bottom:12px;padding-left:3.75%;padding-right:3.75%;margin:0;width:92.5%}._23tra1HsiiP6cT-Cka-ycB{display:block}._1XuCi2WhiqeWRUVp3pnFG3{margin-bottom:8px;margin-left:0;margin-right:0;width:100%}._2bvsb3ubApyZ0UGoQA9O9T{overflow:hidden}.AFsJE948muYyzCMktdzuk{top:1.8%;width:93.33%;height:96.4%;overflow:hidden}.uCYvKvHXrhjNgflv1VqdD{margin-top:24px;margin-left:24px;margin-right:24px;height:100%}._1kBkHQ1V1wu3kl-YcLgUr6{height:62%;height:calc(100% - 188px);min-height:50%}._2uhaEsmeotZ3P-M0AXo2kF{width:100%}._3tOu1FJ59c_xz_PmI1lKV5{margin-bottom:12px;margin-left:0;width:100%}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0 0 12px 0;padding:0;float:none}}@media only screen and (max-width: 768px) and (orientation: landscape), only screen and (max-height: 260px), only screen and (max-width: 340px){.AFsJE948muYyzCMktdzuk{overflow:auto}}@media only screen and (max-height: 260px), only screen and (max-width: 340px){._1XuCi2WhiqeWRUVp3pnFG3{min-width:0}._3kWyBRbW_dgnMiEyx06Fu4{padding:3%}.uCYvKvHXrhjNgflv1VqdD{margin-top:3%;margin-left:3%;margin-right:3%}._17pX1m9O_W--iZbDt3Ta5r{margin-bottom:3%}._1kBkHQ1V1wu3kl-YcLgUr6{height:calc(79% - 64px)}.nohp3sIG12ZBhzcMnPala{margin-top:5%;margin-bottom:10%}._3tOu1FJ59c_xz_PmI1lKV5{margin-bottom:3%}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0 0 3% 0;padding:0;float:none}}
</style><style type="text/css" id="ms-consent-banner-theme-styles">._23tra1HsiiP6cT-Cka-ycB {
            background-color: #24292f !important;
        }.w8hcgFksdo30C8w-bygqu {
            color: #ffffff !important;
        }.ydkKdaztSS0AeHWIeIHsQ a {
            color: #d8b9ff !important;
        }._2bvsb3ubApyZ0UGoQA9O9T {
            background-color: rgba(23, 23, 23, 0.8) !important;
        }.AFsJE948muYyzCMktdzuk {
            background-color: #24292f !important;
            border: 1px solid #d8b9ff !important;
        }._3kWyBRbW_dgnMiEyx06Fu4 {
            color: #d8b9ff !important;
            background-color: #24292f !important;
        }._1zNQOqxpBFSokeCLGi_hGr {
            border: 1px solid #ffffff !important;
            background-color: #ffffff !important;
            color: #1f2328 !important;
        }._1zNQOqxpBFSokeCLGi_hGr:enabled:hover {
            color: #1f2328 !important;
            background-color: #d8b9ff !important;
            box-shadow: none !important;
            border: 1px solid transparent !important;
        }._1zNQOqxpBFSokeCLGi_hGr:enabled:focus {
            background-color: #d8b9ff !important;
            box-shadow: none !important;
            border: 2px solid #ffffff !important;
        }._1zNQOqxpBFSokeCLGi_hGr:disabled {
            opacity: 0.5 !important;
            color: #1f2328 !important;
            background-color: #ffffff !important;
            border: 1px solid transparent !important;
        }.erL690_8JwUW-R4bJRcfl {
            border: 1px solid #eaeef2 !important;
            background-color: #32383f !important;
            color: #ffffff !important;
        }.erL690_8JwUW-R4bJRcfl:enabled:hover {
            color: #ffffff !important;
            background-color: #24292f !important;
            box-shadow: none !important;
            border: 1px solid #ffffff !important;
        }.erL690_8JwUW-R4bJRcfl:enabled:focus {
            background-color: #24292f !important;
            box-shadow: none !important;
            border: 2px solid #6e7781 !important;
        }.erL690_8JwUW-R4bJRcfl:disabled {
            opacity: 0.5 !important;
            color: #ffffff !important;
            background-color: #424a53 !important;
            border: 1px solid #6e7781 !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label::before {
            border: 1px solid #d8b9ff !important;
            background-color: #24292f !important;
        }._1HSFn0HzGo6w4ADApV8-c4 {
            outline: 2px solid #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked + label::after {
            background-color: #d8b9ff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:hover::before {
            border: 1px solid #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:hover::after {
            background-color: #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:focus::before {
            border: 1px solid #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:focus::after {
            background-color: #d8b9ff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled + label::before {
            border: 1px solid rgba(227, 227, 227, 0.2) !important;
            background-color: rgba(227, 227, 227, 0.2) !important;
        }</style><link rel="stylesheet" type="text/css" href="./blue_filter_files/74667.1ec9c5dbf510cfa3af4a.module.css" crossorigin="anonymous"></head>

  <body class="logged-in env-production page-responsive" style="overflow-wrap: break-word; --dialog-scrollgutter: 15px;">
    <div data-turbo-body="" class="logged-in env-production page-responsive" style="word-wrap: break-word;">
      <div id="__primerPortalRoot__" role="region" style="z-index: 1000; position: absolute; width: 100%;" data-turbo-permanent=""></div>
      



    <div class="position-relative header-wrapper js-header-wrapper ">
      <a href="https://github.com/SharmilaShroff/image-processing.py#start-of-content" data-skip-target-assigned="false" class="p-3 color-bg-accent-emphasis color-fg-on-emphasis show-on-focus js-skip-to-content">Skip to content</a>

      <span data-view-component="true" class="progress-pjax-loader Progress position-fixed width-full">
    <span style="width: 0%;" data-view-component="true" class="Progress-item progress-pjax-loader-bar left-0 top-0 color-bg-accent-emphasis"></span>
</span>      
      
      <link crossorigin="anonymous" media="all" rel="stylesheet" href="./blue_filter_files/primer-react.47239ec6cbe68138fe4c.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./blue_filter_files/keyboard-shortcuts-dialog.29aaeaafa90f007c6f61.module.css">

<react-partial partial-name="keyboard-shortcuts-dialog" data-ssr="false" data-attempted-ssr="false" data-react-profiling="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"docsUrl":"https://docs.github.com/get-started/accessibility/keyboard-shortcuts"}}</script>
  <div data-target="react-partial.reactRoot"><div class="d-none"></div><script type="application/json" id="__PRIMER_DATA_:r0:__">{"resolvedServerColorMode":"day"}</script></div>
</react-partial>





      

          

                  <header class="AppHeader" role="banner">
      <h2 class="sr-only">Navigation Menu</h2>


        

        <div class="AppHeader-globalBar pb-2 js-global-bar">
          <div class="AppHeader-globalBar-start responsive-context-region">
            <div class="">
                      <react-partial-anchor data-catalyst="">
        <button data-target="react-partial-anchor.anchor" aria-label="Open global navigation menu" show_tooltip="false" type="button" data-view-component="true" class="AppHeader-button Button--secondary Button--medium Button p-0 color-fg-muted" aria-expanded="false" aria-haspopup="true">  <span class="Button-content">
    <span class="Button-label"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-three-bars">
    <path d="M1 2.75A.75.75 0 0 1 1.75 2h12.5a.75.75 0 0 1 0 1.5H1.75A.75.75 0 0 1 1 2.75Zm0 5A.75.75 0 0 1 1.75 7h12.5a.75.75 0 0 1 0 1.5H1.75A.75.75 0 0 1 1 7.75ZM1.75 12h12.5a.75.75 0 0 1 0 1.5H1.75a.75.75 0 0 1 0-1.5Z"></path>
</svg></span>
  </span>
</button>
        
      
          <link crossorigin="anonymous" media="all" rel="stylesheet" href="./blue_filter_files/primer-react.47239ec6cbe68138fe4c.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./blue_filter_files/90759.a752e1d5a8c3aad1a210.module.css">

<react-partial partial-name="global-nav-menu" data-ssr="false" data-attempted-ssr="false" data-react-profiling="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"home":{"href":"/dashboard","hotkey":"g d"},"feed":{"show":false,"href":"/feed"},"issues":{"href":"/issues","hotkey":"g i"},"pulls":{"href":"/pulls","hotkey":"g p"},"contributedRepos":{"show":true,"href":"https://github.com/repos","hotkey":null},"projects":{"href":"/projects"},"discussions":{"show":true,"href":"/discussions"},"codespaces":{"show":true,"href":"https://github.com/codespaces"},"copilot":{"show":true,"href":"/copilot"},"spark":{"show":false,"href":null},"marketplace":{"show":true,"href":"/marketplace"},"mcp":{"show":true,"href":"https://github.com/mcp"},"explore":{"show":true,"href":"/explore"},"richContent":{"show":true,"contentUrl":"/_side-panels/global.json","repositoriesSearchUrl":"/_side-panel-items/global/repositories.json","teamsSearchUrl":"/_side-panel-items/global/teams.json"}}}</script>
  <div data-target="react-partial.reactRoot"><div class="d-none"><li data-has-description="false" class="prc-ActionList-ActionListItem-So4vC"><a class="prc-ActionList-ActionListContent-KBb8- prc-Link-Link-9ZwDx" tabindex="0" aria-labelledby=":ra:--label  " id=":ra:" data-size="medium" href="https://github.com/dashboard" data-testid="side-nav-menu-item-HOME" style="--subitem-depth: 0;"><span class="prc-ActionList-Spacer-4tR2m"></span><span class="prc-ActionList-LeadingVisual-NBr28 prc-ActionList-VisualWrap-bdCsS"><svg aria-hidden="true" focusable="false" class="octicon octicon-home" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M6.906.664a1.749 1.749 0 0 1 2.187 0l5.25 4.2c.415.332.657.835.657 1.367v7.019A1.75 1.75 0 0 1 13.25 15h-3.5a.75.75 0 0 1-.75-.75V9H7v5.25a.75.75 0 0 1-.75.75h-3.5A1.75 1.75 0 0 1 1 13.25V6.23c0-.531.242-1.034.657-1.366l5.25-4.2Zm1.25 1.171a.25.25 0 0 0-.312 0l-5.25 4.2a.25.25 0 0 0-.094.196v7.019c0 .138.112.25.25.25H5.5V8.25a.75.75 0 0 1 .75-.75h3.5a.75.75 0 0 1 .75.75v5.25h2.75a.25.25 0 0 0 .25-.25V6.23a.25.25 0 0 0-.094-.195Z"></path></svg></span><span class="prc-ActionList-ActionListSubContent-gKsFp" data-component="ActionList.Item--DividerContainer"><span id=":ra:--label" class="prc-ActionList-ItemLabel-81ohH">Home</span></span></a></li><li data-has-description="false" class="prc-ActionList-ActionListItem-So4vC"><a class="prc-ActionList-ActionListContent-KBb8- prc-Link-Link-9ZwDx" tabindex="0" aria-labelledby=":rb:--label  " id=":rb:" data-size="medium" href="https://github.com/issues" data-testid="side-nav-menu-item-ISSUES" style="--subitem-depth: 0;"><span class="prc-ActionList-Spacer-4tR2m"></span><span class="prc-ActionList-LeadingVisual-NBr28 prc-ActionList-VisualWrap-bdCsS"><svg aria-hidden="true" focusable="false" class="octicon octicon-issue-opened" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path></svg></span><span class="prc-ActionList-ActionListSubContent-gKsFp" data-component="ActionList.Item--DividerContainer"><span id=":rb:--label" class="prc-ActionList-ItemLabel-81ohH">Issues</span></span></a></li><li data-has-description="false" class="prc-ActionList-ActionListItem-So4vC"><a class="prc-ActionList-ActionListContent-KBb8- prc-Link-Link-9ZwDx" tabindex="0" aria-labelledby=":rc:--label  " id=":rc:" data-size="medium" href="https://github.com/pulls" data-testid="side-nav-menu-item-PULL_REQUESTS" style="--subitem-depth: 0;"><span class="prc-ActionList-Spacer-4tR2m"></span><span class="prc-ActionList-LeadingVisual-NBr28 prc-ActionList-VisualWrap-bdCsS"><svg aria-hidden="true" focusable="false" class="octicon octicon-git-pull-request" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path></svg></span><span class="prc-ActionList-ActionListSubContent-gKsFp" data-component="ActionList.Item--DividerContainer"><span id=":rc:--label" class="prc-ActionList-ItemLabel-81ohH">Pull requests</span></span></a></li></div><script type="application/json" id="__PRIMER_DATA_:r9:__">{"resolvedServerColorMode":"day"}</script></div>
</react-partial>


        </react-partial-anchor>

            </div>

            <a class="AppHeader-logo ml-1 " href="https://github.com/" data-hotkey="g d" aria-label="Homepage " data-turbo="false" data-analytics-event="{&quot;category&quot;:&quot;Header&quot;,&quot;action&quot;:&quot;go to dashboard&quot;,&quot;label&quot;:&quot;icon:logo&quot;}">
              <svg height="32" aria-hidden="true" viewBox="0 0 24 24" version="1.1" width="32" data-view-component="true" class="octicon octicon-mark-github v-align-middle">
    <path d="M12 1C5.923 1 1 5.923 1 12c0 4.867 3.149 8.979 7.521 10.436.55.096.756-.233.756-.522 0-.262-.013-1.128-.013-2.049-2.764.509-3.479-.674-3.699-1.292-.124-.317-.66-1.293-1.127-1.554-.385-.207-.936-.715-.014-.729.866-.014 1.485.797 1.691 1.128.99 1.663 2.571 1.196 3.204.907.096-.715.385-1.196.701-1.471-2.448-.275-5.005-1.224-5.005-5.432 0-1.196.426-2.186 1.128-2.956-.111-.275-.496-1.402.11-2.915 0 0 .921-.288 3.024 1.128a10.193 10.193 0 0 1 2.75-.371c.936 0 1.871.123 2.75.371 2.104-1.43 3.025-1.128 3.025-1.128.605 1.513.221 2.64.111 2.915.701.77 1.127 1.747 1.127 2.956 0 4.222-2.571 5.157-5.019 5.432.399.344.743 1.004.743 2.035 0 1.471-.014 2.654-.014 3.025 0 .289.206.632.756.522C19.851 20.979 23 16.854 23 12c0-6.077-4.922-11-11-11Z"></path>
</svg>
            </a>

              <context-region-controller class="AppHeader-context responsive-context-region" data-max-items="5" data-catalyst="">
  <div class="AppHeader-context-full">
    <nav role="navigation" aria-label="GitHub Breadcrumb">
      
<context-region data-target="context-region-controller.contextRegion" role="list" data-action="context-region-changed:context-region-controller#crumbsChanged" data-catalyst="">
    <context-region-crumb data-crumb-id="contextregion-usercrumb-sharmilashroff" data-targets="context-region.crumbs" data-label="SharmilaShroff" data-href="/SharmilaShroff" data-pre-rendered="" role="listitem" data-catalyst="">
      <a data-target="context-region-crumb.linkElement" data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;SharmilaShroff&quot;,&quot;screen_size&quot;:&quot;full&quot;}" data-hovercard-type="user" data-hovercard-url="/users/SharmilaShroff/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/SharmilaShroff" id="contextregion-usercrumb-sharmilashroff-link" data-view-component="true" class="AppHeader-context-item" aria-keyshortcuts="Alt+ArrowUp">
        <span data-target="context-region-crumb.labelElement" class="AppHeader-context-item-label ">SharmilaShroff</span>

</a><tool-tip data-target="context-region-crumb.tooltip" for="contextregion-usercrumb-sharmilashroff-link" popover="manual" class="sr-only" position="absolute" data-type="label" data-direction="s" hidden="" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>
          SharmilaShroff
        </tool-tip>
      <context-region-divider data-target="context-region-crumb.dividerElement" data-pre-rendered="" data-catalyst="">
  <span class="AppHeader-context-item-separator">
    <span class="sr-only">/</span>
    <svg width="16" height="16" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <path d="M10.956 1.27994L6.06418 14.7201L5 14.7201L9.89181 1.27994L10.956 1.27994Z" fill="currentcolor"></path>
    </svg>
  </span>
</context-region-divider>

    
        
      </context-region-crumb>

      <li data-target="context-region-controller.overflowMenuContainer context-region.overflowMenuContainer" role="listitem" hidden="">
        <action-menu data-target="context-region-controller.overflowActionMenu" data-select-variant="none" data-view-component="true" data-catalyst="" data-ready="true">
  <focus-group direction="vertical" mnemonics="" retain="">
    <button id="action-menu-d9ac43c6-7f27-47a2-9c7a-33a2315e1e61-button" popovertarget="action-menu-d9ac43c6-7f27-47a2-9c7a-33a2315e1e61-overlay" aria-controls="action-menu-d9ac43c6-7f27-47a2-9c7a-33a2315e1e61-list" aria-haspopup="true" aria-labelledby="tooltip-250727ae-6cb4-42d6-a2c3-0f90241db709" type="button" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal Button-visual">
    <path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path>
</svg>
</button><tool-tip id="tooltip-250727ae-6cb4-42d6-a2c3-0f90241db709" for="action-menu-d9ac43c6-7f27-47a2-9c7a-33a2315e1e61-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Show more breadcrumb items</tool-tip>


<anchored-position data-target="action-menu.overlay" id="action-menu-d9ac43c6-7f27-47a2-9c7a-33a2315e1e61-overlay" anchor="action-menu-d9ac43c6-7f27-47a2-9c7a-33a2315e1e61-button" align="start" side="outside-bottom" anchor-offset="normal" popover="auto" data-view-component="true" style="inset: 4px auto auto 0px;">
  <div data-view-component="true" class="Overlay Overlay--size-auto">
    
      <div data-view-component="true" class="Overlay-body Overlay-body--paddingNone">          <action-list data-catalyst="">
  <div data-view-component="true">
    <ul aria-labelledby="action-menu-d9ac43c6-7f27-47a2-9c7a-33a2315e1e61-button" id="action-menu-d9ac43c6-7f27-47a2-9c7a-33a2315e1e61-list" role="menu" data-view-component="true" class="ActionListWrap--inset ActionListWrap">
        <li hidden="true" data-crumb-id="contextregion-usercrumb-sharmilashroff" data-targets="context-region.overflowCrumbs action-list.items" data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_overflow_menu_crumb&quot;,&quot;label&quot;:&quot;global-navigation&quot;}" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-23df2fea-4cb6-4af5-b63b-2b5712f3cddd" href="https://github.com/SharmilaShroff" role="menuitem" data-view-component="true" class="ActionListContent">
      
        <span data-view-component="true" class="ActionListItem-label">
          SharmilaShroff
</span>      
</a>
  
</li>
        <li hidden="true" data-crumb-id="contextregion-repositorycrumb-image-processing-py" data-targets="context-region.overflowCrumbs action-list.items" data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_overflow_menu_crumb&quot;,&quot;label&quot;:&quot;global-navigation&quot;}" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-37360311-d446-46a9-a7f0-b15c245e0928" href="https://github.com/SharmilaShroff/image-processing.py" role="menuitem" data-view-component="true" class="ActionListContent">
      
        <span data-view-component="true" class="ActionListItem-label">
          image-processing.py
</span>      
</a>
  
</li>
</ul>    
</div></action-list>


</div>
      
</div></anchored-position>  </focus-group>
</action-menu>
  <context-region-divider data-target="context-region-crumb.dividerElement" data-pre-rendered="" data-catalyst="">
  <span class="AppHeader-context-item-separator">
    <span class="sr-only">/</span>
    <svg width="16" height="16" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <path d="M10.956 1.27994L6.06418 14.7201L5 14.7201L9.89181 1.27994L10.956 1.27994Z" fill="currentcolor"></path>
    </svg>
  </span>
</context-region-divider>


      </li>
    <context-region-crumb data-crumb-id="contextregion-repositorycrumb-image-processing-py" data-targets="context-region.crumbs" data-label="image-processing.py" data-href="/SharmilaShroff/image-processing.py" data-pre-rendered="" role="listitem" data-catalyst="">
      <a data-target="context-region-crumb.linkElement" data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;image-processing.py&quot;,&quot;screen_size&quot;:&quot;full&quot;}" href="https://github.com/SharmilaShroff/image-processing.py" aria-current="page" id="contextregion-repositorycrumb-image-processing-py-link" data-view-component="true" class="AppHeader-context-item">
        <span data-target="context-region-crumb.labelElement" class="AppHeader-context-item-label ">image-processing.py</span>

</a><tool-tip data-target="context-region-crumb.tooltip" for="contextregion-repositorycrumb-image-processing-py-link" popover="manual" class="sr-only" position="absolute" data-type="label" data-direction="s" hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>
          image-processing.py
        </tool-tip>
      <context-region-divider data-target="context-region-crumb.dividerElement" data-pre-rendered="" data-catalyst="">
  <span class="AppHeader-context-item-separator">
    <span class="sr-only">/</span>
    <svg width="16" height="16" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <path d="M10.956 1.27994L6.06418 14.7201L5 14.7201L9.89181 1.27994L10.956 1.27994Z" fill="currentcolor"></path>
    </svg>
  </span>
</context-region-divider>

    
        
      </context-region-crumb>

</context-region>

    </nav>
  </div>
</context-region-controller>

          </div>
          <div class="AppHeader-globalBar-end">
              <div class="AppHeader-search">
                  


<qbsearch-input class="search-input" data-scope="repo:SharmilaShroff/image-processing.py" data-custom-scopes-path="/search/custom_scopes" data-delete-custom-scopes-csrf="SrPNde2GNamHwp67TJPFtu47FG5oRtMXWiH-1r2WIq7TiU4uodDswKc-mfC1MKxSDeF0ZKfeoSoHAB1cePtOMA" data-max-custom-scopes="10" data-header-redesign-enabled="true" data-initial-value="" data-blackbird-suggestions-path="/search/suggestions" data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations" data-current-repository="SharmilaShroff/image-processing.py" data-current-org="" data-current-owner="SharmilaShroff" data-logged-in="true" data-copilot-chat-enabled="true" data-nl-search-enabled="false" data-catalyst="">
  <div class="search-input-container search-with-dialog position-relative d-flex flex-row flex-items-center height-auto color-bg-transparent border-0 color-fg-subtle mx-0" data-action="click:qbsearch-input#searchInputContainerClicked">
        
              <button type="button" data-action="click:qbsearch-input#handleExpand" class="AppHeader-button AppHeader-search-whenNarrow" aria-label="Search or jump to…" aria-expanded="false" aria-haspopup="dialog">
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
            </button>


<div class="AppHeader-search-whenRegular">
  <div class="AppHeader-search-wrap AppHeader-search-wrap--hasTrailing">
    <div class="AppHeader-search-control AppHeader-search-control-overflow">
      <label for="AppHeader-searchInput" aria-label="Search or jump to…" class="AppHeader-search-visual--leading">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
      </label>

                  <button type="button" data-target="qbsearch-input.inputButton" data-action="click:qbsearch-input#handleExpand" class="AppHeader-searchButton form-control text-left color-fg-subtle no-wrap placeholder" data-hotkey="s,/" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;searchbar&quot;,&quot;context&quot;:&quot;global&quot;,&quot;tag&quot;:&quot;input&quot;,&quot;label&quot;:&quot;searchbar_input_global_navbar&quot;}" aria-describedby="search-error-message-flash">
              <div class="overflow-hidden">
                <span id="qb-input-query" data-target="qbsearch-input.inputButtonText">
                    Type <kbd class="AppHeader-search-kbd">/</kbd> to search
                </span>
              </div>
            </button>

    </div>


  </div>
</div>

    <input type="hidden" name="type" class="js-site-search-type-field">

    
<div class="Overlay--hidden " data-modal-dialog-overlay="">
  <modal-dialog data-action="close:qbsearch-input#handleClose cancel:qbsearch-input#handleClose" data-target="qbsearch-input.searchSuggestionsDialog" role="dialog" id="search-suggestions-dialog" aria-modal="true" aria-labelledby="search-suggestions-dialog-header" data-view-component="true" class="Overlay Overlay--width-medium Overlay--height-auto">
      <h1 id="search-suggestions-dialog-header" class="sr-only">Search code, repositories, users, issues, pull requests...</h1>
    <div class="Overlay-body Overlay-body--paddingNone">
      
          <div data-view-component="true">        <div class="search-suggestions position-absolute width-full color-shadow-large border color-fg-default color-bg-default overflow-hidden d-flex flex-column query-builder-container" style="border-radius: 12px;" data-target="qbsearch-input.queryBuilderContainer" hidden="">
          <!-- '"` --><!-- </textarea></xmp> --><form id="query-builder-test-form" action="https://github.com/SharmilaShroff/image-processing.py" accept-charset="UTF-8" method="get">
  <query-builder data-target="qbsearch-input.queryBuilder" id="query-builder-query-builder-test" data-filter-key=":" data-view-component="true" class="QueryBuilder search-query-builder" data-min-width="300" data-catalyst="">
    <div class="FormControl FormControl--fullWidth">
      <label id="query-builder-test-label" for="query-builder-test" class="FormControl-label sr-only">
        Search
      </label>
      <div class="QueryBuilder-StyledInput width-fit " data-target="query-builder.styledInput">
          <span id="query-builder-test-leadingvisual-wrap" class="FormControl-input-leadingVisualWrap QueryBuilder-leadingVisualWrap">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search FormControl-input-leadingVisual">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
          </span>
        <div data-target="query-builder.styledInputContainer" class="QueryBuilder-StyledInputContainer">
          <div aria-hidden="true" class="QueryBuilder-StyledInputContent" data-target="query-builder.styledInputContent"></div>
          <div class="QueryBuilder-InputWrapper">
            <div aria-hidden="true" class="QueryBuilder-Sizer" data-target="query-builder.sizer"><span></span></div>
            <input id="query-builder-test" name="query-builder-test" value="" autocomplete="off" type="text" role="combobox" spellcheck="false" aria-expanded="false" aria-describedby="validation-289ed0f0-0e5c-4e63-a9a3-b007c96b2ddd" data-target="query-builder.input" data-action="
          input:query-builder#inputChange
          blur:query-builder#inputBlur
          keydown:query-builder#inputKeydown
          focus:query-builder#inputFocus
        " data-view-component="true" class="FormControl-input QueryBuilder-Input FormControl-medium" aria-controls="query-builder-test-results" aria-autocomplete="list" aria-haspopup="listbox" style="width: 300px;">
          </div>
        </div>
          <span class="sr-only" id="query-builder-test-clear">Clear</span>
          <button role="button" id="query-builder-test-clear-button" aria-labelledby="query-builder-test-clear query-builder-test-label" data-target="query-builder.clearButton" data-action="
                click:query-builder#clear
                focus:query-builder#clearButtonFocus
                blur:query-builder#clearButtonBlur
              " variant="small" hidden="" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium mr-1 px-2 py-0 d-flex flex-items-center rounded-1 color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x-circle-fill Button-visual">
    <path d="M2.343 13.657A8 8 0 1 1 13.658 2.343 8 8 0 0 1 2.343 13.657ZM6.03 4.97a.751.751 0 0 0-1.042.018.751.751 0 0 0-.018 1.042L6.94 8 4.97 9.97a.749.749 0 0 0 .326 1.275.749.749 0 0 0 .734-.215L8 9.06l1.97 1.97a.749.749 0 0 0 1.275-.326.749.749 0 0 0-.215-.734L9.06 8l1.97-1.97a.749.749 0 0 0-.326-1.275.749.749 0 0 0-.734.215L8 6.94Z"></path>
</svg>
</button>

      </div>
      <template id="search-icon"></template>

<template id="code-icon"></template>

<template id="file-code-icon"></template>

<template id="history-icon"></template>

<template id="repo-icon"></template>

<template id="bookmark-icon"></template>

<template id="plus-circle-icon"></template>

<template id="circle-icon"></template>

<template id="trash-icon"></template>

<template id="team-icon"></template>

<template id="project-icon"></template>

<template id="pencil-icon"></template>

<template id="copilot-icon"></template>

<template id="copilot-error-icon"></template>

<template id="workflow-icon"></template>

<template id="book-icon"></template>

<template id="code-review-icon"></template>

<template id="codespaces-icon"></template>

<template id="comment-icon"></template>

<template id="comment-discussion-icon"></template>

<template id="organization-icon"></template>

<template id="rocket-icon"></template>

<template id="shield-check-icon"></template>

<template id="heart-icon"></template>

<template id="server-icon"></template>

<template id="globe-icon"></template>

<template id="issue-opened-icon"></template>

<template id="device-mobile-icon"></template>

<template id="package-icon"></template>

<template id="credit-card-icon"></template>

<template id="play-icon"></template>

<template id="gift-icon"></template>

<template id="code-square-icon"></template>

<template id="device-desktop-icon"></template>

        <div class="position-relative">
                <ul role="listbox" class="ActionListWrap QueryBuilder-ListWrap" aria-label="Suggestions" data-action="
                    combobox-commit:query-builder#comboboxCommit
                    mousedown:query-builder#resultsMousedown
                  " data-target="query-builder.resultsList" data-persist-list="false" id="query-builder-test-results" tabindex="-1"></ul>
        </div>
      <div class="FormControl-inlineValidation" id="validation-289ed0f0-0e5c-4e63-a9a3-b007c96b2ddd" hidden="hidden">
        <span class="FormControl-inlineValidation--visual">
          <svg aria-hidden="true" height="12" viewBox="0 0 12 12" version="1.1" width="12" data-view-component="true" class="octicon octicon-alert-fill">
    <path d="M4.855.708c.5-.896 1.79-.896 2.29 0l4.675 8.351a1.312 1.312 0 0 1-1.146 1.954H1.33A1.313 1.313 0 0 1 .183 9.058ZM7 7V3H5v4Zm-1 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z"></path>
</svg>
        </span>
        <span></span>
</div>    </div>
    <div data-target="query-builder.screenReaderFeedback" aria-live="polite" aria-atomic="true" class="sr-only">0 suggestions.</div>
</query-builder></form>
          <div class="d-flex flex-row color-fg-muted px-3 text-small color-bg-default search-feedback-prompt">
            <a target="_blank" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax" data-view-component="true" class="Link color-fg-accent text-normal ml-2">Search syntax tips</a>            <div class="d-flex flex-1"></div>
              <button data-action="click:qbsearch-input#showFeedbackDialog" type="button" data-view-component="true" class="Button--link Button--medium Button color-fg-accent text-normal ml-2">  <span class="Button-content">
    <span class="Button-label">Give feedback</span>
  </span>
</button>
          </div>
        </div>
</div>

    </div>
</modal-dialog></div>
  </div>
  <div data-action="click:qbsearch-input#retract" class="dark-backdrop position-fixed" hidden="" data-target="qbsearch-input.darkBackdrop"></div>
  <div class="color-fg-default">
    
<dialog-helper>
  <dialog data-target="qbsearch-input.feedbackDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="feedback-dialog" aria-modal="true" aria-labelledby="feedback-dialog-title" aria-describedby="feedback-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade Overlay--disableScroll">
    <div data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="feedback-dialog-title">
        Provide feedback
      </h1>
        
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="feedback-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="feedback-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">        <!-- '"` --><!-- </textarea></xmp> --><form id="code-search-feedback-form" data-turbo="false" action="https://github.com/search/feedback" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="Y3qrBrIrM5EhL0jFrkGTKrelVYQRsLmnThoviJB2gYst4EZp05xAQ3TVxFvD4oSCW_JpZcWzJzd3vRuKJiCvcA">
          <p>We read every piece of feedback, and take your input very seriously.</p>
          <textarea name="feedback" class="form-control width-full mb-2" style="height: 120px" id="feedback"></textarea>
          <input name="include_email" id="include_email" aria-label="Include my email address so I can be contacted" class="form-control mr-2" type="checkbox">
          <label for="include_email" style="font-weight: normal">Include my email address so I can be contacted</label>
</form></div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd">          <button data-close-dialog-id="feedback-dialog" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="code-search-feedback-form" data-action="click:qbsearch-input#submitFeedback" type="submit" data-view-component="true" class="btn-primary btn">    Submit feedback
</button>
</div>
</dialog></dialog-helper>

    <custom-scopes data-target="qbsearch-input.customScopesManager" data-catalyst="">
    
<dialog-helper>
  <dialog data-target="custom-scopes.customScopesModalDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="custom-scopes-dialog" aria-modal="true" aria-labelledby="custom-scopes-dialog-title" aria-describedby="custom-scopes-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade Overlay--disableScroll">
    <div data-view-component="true" class="Overlay-header Overlay-header--divided">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="custom-scopes-dialog-title">
        Saved searches
      </h1>
        <h2 id="custom-scopes-dialog-description" class="Overlay-description">Use saved searches to filter your results more quickly</h2>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="custom-scopes-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="custom-scopes-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">        <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

        <div hidden="" class="create-custom-scope-form" data-target="custom-scopes.createCustomScopeForm">
        <!-- '"` --><!-- </textarea></xmp> --><form id="custom-scopes-dialog-form" data-turbo="false" action="https://github.com/search/custom_scopes" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="0KJ3LMKwh8asD6hAJzPDiSHKNF75jak7LrvrUCNG42r36OQeq0hJ6AM47mq4vcwRoGs0HBM-K8QGFzd0C4NPSw">
          <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

          <input type="hidden" id="custom_scope_id" name="custom_scope_id" data-target="custom-scopes.customScopesIdField">

          <div class="form-group">
            <label for="custom_scope_name">Name</label>
            <auto-check src="/search/custom_scopes/check_name" required="">
              <input type="text" name="custom_scope_name" id="custom_scope_name" data-target="custom-scopes.customScopesNameField" class="form-control" autocomplete="off" placeholder="github-ruby" required="" maxlength="50" spellcheck="false">
              <input type="hidden" value="u0405vpDUdjouEjm-Ba-_TW7GhKIADzlsdbCZGVP93SmAlc4DykHTu-UoCLGNTsGZw_VPiLwKGm0R3WDHRn9bQ" data-csrf="true">
            </auto-check>
          </div>

          <div class="form-group">
            <label for="custom_scope_query">Query</label>
            <input type="text" name="custom_scope_query" id="custom_scope_query" data-target="custom-scopes.customScopesQueryField" class="form-control" autocomplete="off" placeholder="(repo:mona/a OR repo:mona/b) AND lang:python" required="" maxlength="500">
          </div>

          <p class="text-small color-fg-muted">
            To see all available qualifiers, see our <a class="Link--inTextBlock" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax">documentation</a>.
          </p>
</form>        </div>

        <div data-target="custom-scopes.manageCustomScopesForm">
          <div data-target="custom-scopes.list"></div>
        </div>

</div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd Overlay-footer--divided">          <button data-action="click:custom-scopes#customScopesCancel" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="custom-scopes-dialog-form" data-action="click:custom-scopes#customScopesSubmit" data-target="custom-scopes.customScopesSubmitButton" type="submit" data-view-component="true" class="btn-primary btn">    Create saved search
</button>
</div>
</dialog></dialog-helper>
    </custom-scopes>
  </div>
</qbsearch-input>  <input type="hidden" value="ffgHYhd4Z3D_nLBB5O5ZzS-ln8sZJL1qvuOW3kCjDI6S4-lUflCPRmDxMg2Ao9IEE9woG1yrJrvjdWxISC2k5g" data-csrf="true" class="js-data-jump-to-suggestions-path-csrf">


              </div>

            
              <div class="AppHeader-CopilotChat hide-sm hide-md">
  <div class="d-flex">
    <react-partial-anchor data-catalyst="">
        <a href="https://github.com/copilot" data-target="react-partial-anchor.anchor" id="copilot-chat-header-button" aria-labelledby="tooltip-d5efe3a2-4fda-4669-9b9c-7ac9aede239d" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button AppHeader-buttonLeft">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copilot Button-visual">
    <path d="M7.998 15.035c-4.562 0-7.873-2.914-7.998-3.749V9.338c.085-.628.677-1.686 1.588-2.065.013-.07.024-.143.036-.218.029-.183.06-.384.126-.612-.201-.508-.254-1.084-.254-1.656 0-.87.128-1.769.693-2.484.579-.733 1.494-1.124 2.724-1.261 1.206-.134 2.262.034 2.944.765.05.053.096.108.139.165.044-.057.094-.112.143-.165.682-.731 1.738-.899 2.944-.765 1.23.137 2.145.528 2.724 1.261.566.715.693 1.614.693 2.484 0 .572-.053 1.148-.254 1.656.066.228.098.429.126.612.012.076.024.148.037.218.924.385 1.522 1.471 1.591 2.095v1.872c0 .766-3.351 3.795-8.002 3.795Zm0-1.485c2.28 0 4.584-1.11 5.002-1.433V7.862l-.023-.116c-.49.21-1.075.291-1.727.291-1.146 0-2.059-.327-2.71-.991A3.222 3.222 0 0 1 8 6.303a3.24 3.24 0 0 1-.544.743c-.65.664-1.563.991-2.71.991-.652 0-1.236-.081-1.727-.291l-.023.116v4.255c.419.323 2.722 1.433 5.002 1.433ZM6.762 2.83c-.193-.206-.637-.413-1.682-.297-1.019.113-1.479.404-1.713.7-.247.312-.369.789-.369 1.554 0 .793.129 1.171.308 1.371.162.181.519.379 1.442.379.853 0 1.339-.235 1.638-.54.315-.322.527-.827.617-1.553.117-.935-.037-1.395-.241-1.614Zm4.155-.297c-1.044-.116-1.488.091-1.681.297-.204.219-.359.679-.242 1.614.091.726.303 1.231.618 1.553.299.305.784.54 1.638.54.922 0 1.28-.198 1.442-.379.179-.2.308-.578.308-1.371 0-.765-.123-1.242-.37-1.554-.233-.296-.693-.587-1.713-.7Z"></path><path d="M6.25 9.037a.75.75 0 0 1 .75.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 .75-.75Zm4.25.75v1.501a.75.75 0 0 1-1.5 0V9.787a.75.75 0 0 1 1.5 0Z"></path>
</svg>
</a><tool-tip id="tooltip-d5efe3a2-4fda-4669-9b9c-7ac9aede239d" for="copilot-chat-header-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Chat with Copilot</tool-tip>

      
    
        <script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/26744-145228b165b8.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/40489-060d59afaf1e.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/18312-17646a9d1ca3.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/347-d8794b0e68a7.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/89332-9740f6e3c202.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/15874-2c3dffc9f79c.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/45230-15943c5d83b7.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/5853-d0a8a3bf6a60.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/16007-a629e97ccd37.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/88324-d7eea3db7970.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/3146-9ca03a5c5e8d.js.download" defer="defer"></script>

<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/29665-96a2ad6dd82d.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/4817-f48561ea4fc0.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/37294-766aafde5db8.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/2635-6f98bf46d58e.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/30721-d937e90148ac.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/99808-2e3a442ab29e.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/52302-afe653ef8c07.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/81171-757517779b01.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/84597-e42fbc8bdcb1.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/34522-d7ca02ef8731.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/92135-24026ed9fcec.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/34031-e8bf85523f93.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/54995-abd7f03fa6d8.js.download" defer="defer"></script>
<script crossorigin="anonymous" type="application/javascript" src="./blue_filter_files/copilot-chat-e5fffef9dd9b.js.download" defer="defer"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./blue_filter_files/primer-react.47239ec6cbe68138fe4c.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./blue_filter_files/54995.240e70b3a144f83c03aa.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./blue_filter_files/copilot-chat.1ec9c5dbf510cfa3af4a.module.css">
        <link crossorigin="anonymous" media="all" rel="stylesheet" href="./blue_filter_files/copilot-markdown-rendering-ddd978d4a7c0.css">
        <link crossorigin="anonymous" media="all" rel="stylesheet" href="./blue_filter_files/primer-react.47239ec6cbe68138fe4c.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./blue_filter_files/54995.240e70b3a144f83c03aa.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./blue_filter_files/copilot-chat.1ec9c5dbf510cfa3af4a.module.css">

<react-partial partial-name="copilot-chat" data-ssr="false" data-attempted-ssr="false" data-react-profiling="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"currentTopic":{"id":1098386497,"name":"image-processing.py","ownerLogin":"SharmilaShroff","ownerType":"User","readmePath":"README.md","description":"A Python script that loads an image, applies a strong box blur using Pillow (PIL), and displays the blurred output with Matplotlib.","commitOID":"dea4000e90744fd0dea754f6bce0c0316ea771cb","ref":"refs/heads/main","refInfo":{"name":"main","type":"branch"},"visibility":"public","languages":[{"name":"Python","percent":100.0}],"customInstructions":[],"defaultBranch":"main","ownerAvatarUrl":"https://avatars.githubusercontent.com/u/190357636?v=4"},"findFileWorkerPath":"/assets-cdn/worker/find-file-worker-0cea8c6113ab.js","renderPopover":false,"renderBetaLabel":false,"chatIsVisible":true,"chatVisibleSettingPath":"/users/SharmilaShroff/copilot_chat/settings/copilot_chat_visibility","ssoOrganizations":[],"agentsPath":"/github-copilot/chat/agents","apiURL":"https://api.individual.githubcopilot.com","apiVersion":"2025-05-01","currentUserLogin":"SharmilaShroff","customInstructions":null,"customCopilotsEnabled":true,"optedInToPreviewFeatures":false,"optedInToUserFeedback":true,"personalInstructions":null,"graphqlApiUrl":"/copilot/loops/loops_execution","loopsClientUrl":"/copilot/loops/client","reviewLab":false,"realIp":null,"scrollToTop":false,"hasCEorCBAccess":false,"licenseType":"licensed_limited","plan":"free","quotas":{"limits":{"premiumInteractions":0},"remaining":{"chat":320,"completions":3843,"premiumInteractions":0,"chatPercentage":64.0,"premiumInteractionsPercentage":0.0},"resetDate":"2026-01-11","overagesEnabled":false},"icebreakers":[{"type":"functional","data":[{"id":"create-bug-issue","message":"Hi Copilot! Could you please start a draft issue for a bug? Once you've created the draft issue, if you need more information, ask me 1-2 key questions. If you also think I should upload any information or images that would help write the bug issue, let me know.","titleHtml":"Create an issue for a bug","icon":"issue-opened","color":"var(--display-green-fgColor)"},{"id":"summarize-pulls","message":"Hi Copilot! Could you help summarize a pull request? I'd like to know its purpose and the key changes made. Please include details about the problem it solves, new features or functionality introduced, any breaking changes, testing done, and documentation updates. Thank you!","titleHtml":"Summarize a pull request","icon":"git-pull-request","color":"var(--display-green-fgColor)"},{"id":"code-feedback","message":"Hi Copilot! Please review my code for best practices, readability, performance, and potential bugs. First, prompt me to provide the link to the relevant GitHub repository or file. Then, offer concrete suggestions for improvement, explain any issues you discover, and provide example corrections where appropriate.","titleHtml":"Get code feedback","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"next-steps-issue","message":"Hi Copilot! Could you suggest the next actionable steps for an issue, based on either the provided issue link or a copy pasted description?","titleHtml":"Suggest next steps for an issue","icon":"issue-opened","color":"var(--display-green-fgColor)"},{"id":"understand-arch-diagram","message":"Hi Copilot! Could you please help me interpret this architecture diagram?","titleHtml":"Interpret an architecture diagram","icon":"eye","color":"var(--display-purple-fgColor)"},{"id":"create-profile-readme","message":"Hi Copilot! Please create a standout profile README for $$USERNAME$$. Ask me for any key details (such as my profession, top skills, favorite projects, or social links) that would help you personalize it.","titleHtml":"Create a profile README for me","icon":"rocket","color":"var(--display-pink-fgColor)"},{"id":"my-open-pulls","message":"Hi Copilot! Can you please find my open pull requests?","titleHtml":"My open pull requests","icon":"git-pull-request","color":"var(--display-green-fgColor)"},{"id":"make-pong","message":"Hi Copilot! Could you generate a simple Pong game utilizing HTML, CSS, and JavaScript? The player should control the left paddle with their mouse, and the right paddle should be controlled automatically by a basic AI. Make sure the game includes a bouncing ball and collision detection for paddles and walls. Please provide the code for all three components: the HTML file, the CSS file, and the JavaScript file directly within the chat window. Thanks!","titleHtml":"Make a Pong game","icon":"code","color":"var(--display-gray-fgColor)"}]},{"type":"instructional","data":[]},{"type":"interactional","data":[{"id":"to-do-app-local-storage","message":"Create a to-do list application with local storage functionality.","titleHtml":"To-do list with local storage","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"digital-clock-time-zones","message":"Create a digital clock that displays the current time in different time zones.","titleHtml":"A digital time zone clock","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"weather-dashboard-app","message":"Develop a weather dashboard that fetches data from a public weather API.","titleHtml":"Develop a weather dashboard","icon":"code","color":"var(--display-gray-fgColor)"},{"id":"create-joke-generator","message":"Create a random joke generator using an external API.","titleHtml":"Create a joke generator","icon":"code","color":"var(--display-gray-fgColor)"}]}],"canShareThread":true,"thirdPartyMcpAllowed":true}}</script>
  <div data-target="react-partial.reactRoot"><div class="CopilotChat-module__CopilotChatContainer--fWXmM"></div><div class="PortalContainerUtils-module__chatPortalContainer--Otmle"></div><div class="PortalContainerUtils-module__menuPortalContainer--D7AeL CopilotChat-module__menuPortalContainer--FUc3K"></div><script type="application/json" id="__PRIMER_DATA_:r12:__">{"resolvedServerColorMode":"day"}</script></div>
</react-partial>



      </react-partial-anchor>
    <div class="position-relative">
      
        <react-partial-anchor data-catalyst="">
          <button id="global-copilot-menu-button" data-target="react-partial-anchor.anchor" aria-expanded="false" aria-labelledby="tooltip-29c389be-a428-4fb2-8f2a-2c5221f4134e" type="button" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button AppHeader-buttonRight" aria-haspopup="true">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-triangle-down Button-visual">
    <path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path>
</svg>
</button><tool-tip id="tooltip-29c389be-a428-4fb2-8f2a-2c5221f4134e" for="global-copilot-menu-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Open Copilot…</tool-tip>

          
        
            <link crossorigin="anonymous" media="all" rel="stylesheet" href="./blue_filter_files/primer-react.47239ec6cbe68138fe4c.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./blue_filter_files/global-copilot-menu.9d926f69ee309a45d0df.module.css">

<react-partial partial-name="global-copilot-menu" data-ssr="false" data-attempted-ssr="false" data-react-profiling="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"repository":{"id":1098386497,"name":"image-processing.py","ownerLogin":"SharmilaShroff"}}}</script>
  <div data-target="react-partial.reactRoot"><div class="d-none"></div><script type="application/json" id="__PRIMER_DATA_:rd:__">{"resolvedServerColorMode":"day"}</script></div>
</react-partial>


          </react-partial-anchor>
    </div>
  </div>
</div>


            <div class="AppHeader-actions position-relative">
                 <react-partial-anchor data-catalyst="">
      <button id="global-create-menu-anchor" aria-label="Create something new" data-target="react-partial-anchor.anchor" type="button" data-view-component="true" class="AppHeader-button AppHeader-button--dropdown global-create-button Button--secondary Button--medium Button width-auto color-fg-muted" aria-describedby="tooltip-e88776ae-4186-4f5b-8980-98544a82ea2a" aria-expanded="false" aria-haspopup="true">  <span class="Button-content">
      <span class="Button-visual Button-leadingVisual">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
      </span>
    <span class="Button-label"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-triangle-down">
    <path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path>
</svg></span>
  </span>
</button><tool-tip id="tooltip-e88776ae-4186-4f5b-8980-98544a82ea2a" for="global-create-menu-anchor" popover="manual" data-direction="s" data-type="description" data-view-component="true" class="sr-only position-absolute" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Create new…</tool-tip>

      
    
        <link crossorigin="anonymous" media="all" rel="stylesheet" href="./blue_filter_files/primer-react.47239ec6cbe68138fe4c.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./blue_filter_files/global-create-menu.30736d4aa7b2b246dd6f.module.css">

<react-partial partial-name="global-create-menu" data-ssr="false" data-attempted-ssr="false" data-react-profiling="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"showCreateRepo":true,"showImportRepo":true,"showCodespaces":true,"showSpark":false,"showCodingAgent":false,"showGist":true,"showCreateOrg":true,"showCreateProject":false,"showCreateLegacyProject":false,"showCreateIssue":true,"createProjectUrl":"/SharmilaShroff?tab=projects","org":null,"owner":"SharmilaShroff","repo":"image-processing.py"}}</script>
  <div data-target="react-partial.reactRoot"><script type="application/json" id="__PRIMER_DATA_:rh:__">{"resolvedServerColorMode":"day"}</script></div>
</react-partial>


      </react-partial-anchor>


                <a href="https://github.com/issues" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;ISSUES_HEADER&quot;,&quot;label&quot;:null}" id="icon-button-51de9978-6f16-4d72-ad5c-54b79c739d8c" aria-labelledby="tooltip-1c0c0abc-f9d4-4b64-a96b-fc179b6bedc9" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened Button-visual">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
</a><tool-tip id="tooltip-1c0c0abc-f9d4-4b64-a96b-fc179b6bedc9" for="icon-button-51de9978-6f16-4d72-ad5c-54b79c739d8c" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Your issues</tool-tip>

                <a href="https://github.com/pulls" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;PULL_REQUESTS_HEADER&quot;,&quot;label&quot;:null}" id="icon-button-74ef928c-9480-4042-b4d7-f071edc744f5" aria-labelledby="tooltip-dbeebe2a-9c5f-43a2-b5a6-9c14b935cfbd" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request Button-visual">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
</a><tool-tip id="tooltip-dbeebe2a-9c5f-43a2-b5a6-9c14b935cfbd" for="icon-button-74ef928c-9480-4042-b4d7-f071edc744f5" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Your pull requests</tool-tip>

                  <a href="https://github.com/repos" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;REPOS_HEADER&quot;,&quot;label&quot;:null}" id="icon-button-0e5eacd5-a1ee-4813-99a2-1d194831c35c" aria-labelledby="tooltip-11a152fa-f25c-4bf5-a6d9-f3601572a129" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo Button-visual">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>
</a><tool-tip id="tooltip-11a152fa-f25c-4bf5-a6d9-f3601572a129" for="icon-button-0e5eacd5-a1ee-4813-99a2-1d194831c35c" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Repositories</tool-tip>

            </div>

              <notification-indicator data-channel="eyJjIjoibm90aWZpY2F0aW9uLWNoYW5nZWQ6MTkwMzU3NjM2IiwidCI6MTc2NzYyNDMwNH0=--0c4cec09e4a41eb94324b87582cbdb32bbc927973a982037a622a20255418989" data-indicator-mode="none" data-tooltip-global="You have unread notifications" data-tooltip-unavailable="Notifications are unavailable at the moment." data-tooltip-none="You have no unread notifications" data-header-redesign-enabled="true" data-fetch-indicator-src="/notifications/indicator" data-fetch-indicator-enabled="true" data-view-component="true" class="js-socket-channel" data-fetch-retry-delay-time="500" data-catalyst="">
    <a id="AppHeader-notifications-button" href="https://github.com/notifications" aria-labelledby="notification-indicator-tooltip" data-hotkey="g n" data-target="notification-indicator.link" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;NOTIFICATIONS_HEADER&quot;,&quot;label&quot;:&quot;icon:read&quot;}" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-inbox Button-visual">
    <path d="M2.8 2.06A1.75 1.75 0 0 1 4.41 1h7.18c.7 0 1.333.417 1.61 1.06l2.74 6.395c.04.093.06.194.06.295v4.5A1.75 1.75 0 0 1 14.25 15H1.75A1.75 1.75 0 0 1 0 13.25v-4.5c0-.101.02-.202.06-.295Zm1.61.44a.25.25 0 0 0-.23.152L1.887 8H4.75a.75.75 0 0 1 .6.3L6.625 10h2.75l1.275-1.7a.75.75 0 0 1 .6-.3h2.863L11.82 2.652a.25.25 0 0 0-.23-.152Zm10.09 7h-2.875l-1.275 1.7a.75.75 0 0 1-.6.3h-3.5a.75.75 0 0 1-.6-.3L4.375 9.5H1.5v3.75c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25Z"></path>
</svg>
</a>

    <tool-tip id="notification-indicator-tooltip" data-target="notification-indicator.tooltip" for="AppHeader-notifications-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>You have no unread notifications</tool-tip>
</notification-indicator>

            <div class="AppHeader-user">
              <deferred-side-panel data-url="/_side-panels/user?repository_id=1098386497" data-catalyst="">
  <include-fragment data-target="deferred-side-panel.fragment" data-nonce="v2:2b815f31-74b1-a9f7-c69b-a73f6467a217" data-view-component="true"><template shadowrootmode="open"><style>:host {display: block;}</style><slot></slot></template>
  
    <react-partial-anchor data-catalyst="">
  <button data-target="react-partial-anchor.anchor" data-login="SharmilaShroff" aria-label="Open user navigation menu" type="button" data-view-component="true" class="Button--invisible Button--medium Button Button--invisible-noVisuals color-bg-transparent p-0" aria-expanded="false" aria-haspopup="true">  <span class="Button-content">
    <span class="Button-label"><img src="./blue_filter_files/190357636" alt="" size="32" height="32" width="32" data-view-component="true" class="avatar circle"></span>
  </span>
</button>
  

    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./blue_filter_files/primer-react.47239ec6cbe68138fe4c.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./blue_filter_files/global-user-nav-drawer.f4d276768bcd7cf634b3.module.css">

<react-partial partial-name="global-user-nav-drawer" data-ssr="false" data-attempted-ssr="false" data-react-profiling="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"owner":{"login":"SharmilaShroff","name":"Sharmila Shroff","avatarUrl":"https://avatars.githubusercontent.com/u/190357636?v=4"},"drawerId":"global-user-nav-drawer","lazyLoadItemDataFetchUrl":"/_side-panels/user.json","canAddAccount":true,"addAccountPath":"/login?add_account=1\u0026return_to=https%3A%2F%2Fgithub.com%2FSharmilaShroff%2Fimage-processing.py","switchAccountPath":"/switch_account","loginAccountPath":"/login?add_account=1","projectsPath":"/SharmilaShroff?tab=projects","gistsUrl":"https://gist.github.com/mine","docsUrl":"https://docs.github.com","yourEnterpriseUrl":null,"enterpriseSettingsUrl":null,"supportUrl":"https://support.github.com","showAccountSwitcher":true,"showCopilot":true,"showEnterprises":true,"showEnterprise":false,"showGists":true,"showOrganizations":true,"showSponsors":true,"showUpgrade":true,"showFeaturesPreviews":true,"showEnterpriseSettings":false}}</script>
  <div data-target="react-partial.reactRoot"><script type="application/json" id="__PRIMER_DATA_:rk:__">{"resolvedServerColorMode":"day"}</script></div>
</react-partial>


  </react-partial-anchor>


  <div data-show-on-forbidden-error="" hidden="">
    <div class="Box">
  <div class="blankslate-container">
    <div data-view-component="true" class="blankslate blankslate-spacious color-bg-default rounded-2">
      

      <h3 data-view-component="true" class="blankslate-heading">        Uh oh!
</h3>
      <p data-view-component="true">        </p><p class="color-fg-muted my-2 mb-2 ws-normal">There was an error while loading. <a class="Link--inTextBlock" data-turbo="false" href="https://github.com/SharmilaShroff/image-processing.py" aria-label="Please reload this page">Please reload this page</a>.</p>
<p></p>

</div>  </div>
</div>  </div>
</include-fragment></deferred-side-panel>
            </div>

            <div class="position-absolute mt-2">
                
<site-header-logged-in-user-menu data-catalyst="">

</site-header-logged-in-user-menu>

            </div>
          </div>
        </div>


        
            <div class="AppHeader-localBar">
              <nav data-pjax="#js-repo-pjax-container" aria-label="Repository" data-view-component="true" class="js-repo-nav js-sidenav-container-pjax js-responsive-underlinenav overflow-hidden UnderlineNav">

  <ul data-view-component="true" class="UnderlineNav-body list-style-none">
      <li data-view-component="true" class="d-inline-flex">
  <a id="code-tab" href="https://github.com/SharmilaShroff/image-processing.py" data-tab-item="i0code-tab" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages repo_deployments repo_attestations /SharmilaShroff/image-processing.py" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g c" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Code&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" aria-current="page" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item selected">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code UnderlineNav-octicon d-none d-sm-inline">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        <span data-content="Code">Code</span>
          <span id="code-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="issues-tab" href="https://github.com/SharmilaShroff/image-processing.py/issues" data-tab-item="i1issues-tab" data-selected-links="repo_issues repo_labels repo_milestones /SharmilaShroff/image-processing.py/issues" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g i" data-react-nav="issues-react" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Issues&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        <span data-content="Issues">Issues</span>
          <span id="issues-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="pull-requests-tab" href="https://github.com/SharmilaShroff/image-processing.py/pulls" data-tab-item="i2pull-requests-tab" data-selected-links="repo_pulls checks /SharmilaShroff/image-processing.py/pulls" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g p" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Pull requests&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        <span data-content="Pull requests">Pull requests</span>
          <span id="pull-requests-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="actions-tab" href="https://github.com/SharmilaShroff/image-processing.py/actions" data-tab-item="i3actions-tab" data-selected-links="repo_actions /SharmilaShroff/image-processing.py/actions" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g a" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Actions&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path>
</svg>
        <span data-content="Actions">Actions</span>
          <span id="actions-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="projects-tab" href="https://github.com/SharmilaShroff/image-processing.py/projects" data-tab-item="i4projects-tab" data-selected-links="repo_projects new_repo_project repo_project /SharmilaShroff/image-processing.py/projects" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g b" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Projects&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table UnderlineNav-octicon d-none d-sm-inline">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path>
</svg>
        <span data-content="Projects">Projects</span>
          <span id="projects-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="wiki-tab" href="https://github.com/SharmilaShroff/image-processing.py/wiki" data-tab-item="i5wiki-tab" data-selected-links="repo_wiki /SharmilaShroff/image-processing.py/wiki" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g w" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Wiki&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-book UnderlineNav-octicon d-none d-sm-inline">
    <path d="M0 1.75A.75.75 0 0 1 .75 1h4.253c1.227 0 2.317.59 3 1.501A3.743 3.743 0 0 1 11.006 1h4.245a.75.75 0 0 1 .75.75v10.5a.75.75 0 0 1-.75.75h-4.507a2.25 2.25 0 0 0-1.591.659l-.622.621a.75.75 0 0 1-1.06 0l-.622-.621A2.25 2.25 0 0 0 5.258 13H.75a.75.75 0 0 1-.75-.75Zm7.251 10.324.004-5.073-.002-2.253A2.25 2.25 0 0 0 5.003 2.5H1.5v9h3.757a3.75 3.75 0 0 1 1.994.574ZM8.755 4.75l-.004 7.322a3.752 3.752 0 0 1 1.992-.572H14.5v-9h-3.495a2.25 2.25 0 0 0-2.25 2.25Z"></path>
</svg>
        <span data-content="Wiki">Wiki</span>
          <span id="wiki-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="security-tab" href="https://github.com/SharmilaShroff/image-processing.py/security" data-tab-item="i6security-tab" data-selected-links="security overview alerts policy token_scanning code_scanning /SharmilaShroff/image-processing.py/security" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g s" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Security&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-shield UnderlineNav-octicon d-none d-sm-inline">
    <path d="M7.467.133a1.748 1.748 0 0 1 1.066 0l5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667Zm.61 1.429a.25.25 0 0 0-.153 0l-5.25 1.68a.25.25 0 0 0-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.196.196 0 0 0 .154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.251.251 0 0 0-.174-.237l-5.25-1.68ZM8.75 4.75v3a.75.75 0 0 1-1.5 0v-3a.75.75 0 0 1 1.5 0ZM9 10.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span data-content="Security">Security</span>
          </a><div data-show-on-forbidden-error="" hidden=""><a id="security-tab" href="https://github.com/SharmilaShroff/image-processing.py/security" data-tab-item="i6security-tab" data-selected-links="security overview alerts policy token_scanning code_scanning /SharmilaShroff/image-processing.py/security" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g s" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Security&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    </a><div class="Box"><a id="security-tab" href="https://github.com/SharmilaShroff/image-processing.py/security" data-tab-item="i6security-tab" data-selected-links="security overview alerts policy token_scanning code_scanning /SharmilaShroff/image-processing.py/security" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g s" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Security&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
  </a><div class="blankslate-container"><a id="security-tab" href="https://github.com/SharmilaShroff/image-processing.py/security" data-tab-item="i6security-tab" data-selected-links="security overview alerts policy token_scanning code_scanning /SharmilaShroff/image-processing.py/security" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g s" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Security&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    </a><div data-view-component="true" class="blankslate blankslate-spacious color-bg-default rounded-2"><a id="security-tab" href="https://github.com/SharmilaShroff/image-processing.py/security" data-tab-item="i6security-tab" data-selected-links="security overview alerts policy token_scanning code_scanning /SharmilaShroff/image-processing.py/security" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g s" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Security&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
      

      <h3 data-view-component="true" class="blankslate-heading">        Uh oh!
</h3>
      <p data-view-component="true">        </p></a><p class="color-fg-muted my-2 mb-2 ws-normal"><a id="security-tab" href="https://github.com/SharmilaShroff/image-processing.py/security" data-tab-item="i6security-tab" data-selected-links="security overview alerts policy token_scanning code_scanning /SharmilaShroff/image-processing.py/security" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g s" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Security&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">There was an error while loading. </a><a class="Link--inTextBlock" data-turbo="false" href="https://github.com/SharmilaShroff/image-processing.py" aria-label="Please reload this page">Please reload this page</a>.</p>
<p></p>

</div>  </div>
</div>  </div>


    
</li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="insights-tab" href="https://github.com/SharmilaShroff/image-processing.py/pulse" data-tab-item="i7insights-tab" data-selected-links="repo_graphs repo_contributors dependency_graph dependabot_updates pulse people community /SharmilaShroff/image-processing.py/pulse" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Insights&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-graph UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 1.75V13.5h13.75a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1-.75-.75V1.75a.75.75 0 0 1 1.5 0Zm14.28 2.53-5.25 5.25a.75.75 0 0 1-1.06 0L7 7.06 4.28 9.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.25-3.25a.75.75 0 0 1 1.06 0L10 7.94l4.72-4.72a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
        <span data-content="Insights">Insights</span>
          <span id="insights-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="settings-tab" href="https://github.com/SharmilaShroff/image-processing.py/settings" data-tab-item="i8settings-tab" data-selected-links="code_review_limits code_quality codespaces_repository_settings collaborators custom_tabs github_models_repo_settings hooks integration_installations interaction_limits issue_template_editor key_links_settings license_policy notifications repo_announcements repo_branch_settings repo_custom_properties repo_keys_settings repo_pages_settings repo_protected_tags_settings repo_rule_insights repo_rules_bypass_requests repo_rulesets repo_settings_copilot_coding_guidelines repo_settings_copilot_content_exclusion repo_settings_copilot_swe_agent repo_settings reported_content repository_actions_settings_add_new_runner repository_actions_settings_general repository_actions_settings_runner_details repository_actions_settings_runners repository_actions_settings repository_environments role_details secrets_settings_actions secrets_settings_codespaces secrets_settings_dependabot secrets security_analysis security_products /SharmilaShroff/image-processing.py/settings" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Settings&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-gear UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 0a8.2 8.2 0 0 1 .701.031C9.444.095 9.99.645 10.16 1.29l.288 1.107c.018.066.079.158.212.224.231.114.454.243.668.386.123.082.233.09.299.071l1.103-.303c.644-.176 1.392.021 1.82.63.27.385.506.792.704 1.218.315.675.111 1.422-.364 1.891l-.814.806c-.049.048-.098.147-.088.294.016.257.016.515 0 .772-.01.147.038.246.088.294l.814.806c.475.469.679 1.216.364 1.891a7.977 7.977 0 0 1-.704 1.217c-.428.61-1.176.807-1.82.63l-1.102-.302c-.067-.019-.177-.011-.3.071a5.909 5.909 0 0 1-.668.386c-.133.066-.194.158-.211.224l-.29 1.106c-.168.646-.715 1.196-1.458 1.26a8.006 8.006 0 0 1-1.402 0c-.743-.064-1.289-.614-1.458-1.26l-.289-1.106c-.018-.066-.079-.158-.212-.224a5.738 5.738 0 0 1-.668-.386c-.123-.082-.233-.09-.299-.071l-1.103.303c-.644.176-1.392-.021-1.82-.63a8.12 8.12 0 0 1-.704-1.218c-.315-.675-.111-1.422.363-1.891l.815-.806c.05-.048.098-.147.088-.294a6.214 6.214 0 0 1 0-.772c.01-.147-.038-.246-.088-.294l-.815-.806C.635 6.045.431 5.298.746 4.623a7.92 7.92 0 0 1 .704-1.217c.428-.61 1.176-.807 1.82-.63l1.102.302c.067.019.177.011.3-.071.214-.143.437-.272.668-.386.133-.066.194-.158.211-.224l.29-1.106C6.009.645 6.556.095 7.299.03 7.53.01 7.764 0 8 0Zm-.571 1.525c-.036.003-.108.036-.137.146l-.289 1.105c-.147.561-.549.967-.998 1.189-.173.086-.34.183-.5.29-.417.278-.97.423-1.529.27l-1.103-.303c-.109-.03-.175.016-.195.045-.22.312-.412.644-.573.99-.014.031-.021.11.059.19l.815.806c.411.406.562.957.53 1.456a4.709 4.709 0 0 0 0 .582c.032.499-.119 1.05-.53 1.456l-.815.806c-.081.08-.073.159-.059.19.162.346.353.677.573.989.02.03.085.076.195.046l1.102-.303c.56-.153 1.113-.008 1.53.27.161.107.328.204.501.29.447.222.85.629.997 1.189l.289 1.105c.029.109.101.143.137.146a6.6 6.6 0 0 0 1.142 0c.036-.003.108-.036.137-.146l.289-1.105c.147-.561.549-.967.998-1.189.173-.086.34-.183.5-.29.417-.278.97-.423 1.529-.27l1.103.303c.109.029.175-.016.195-.045.22-.313.411-.644.573-.99.014-.031.021-.11-.059-.19l-.815-.806c-.411-.406-.562-.957-.53-1.456a4.709 4.709 0 0 0 0-.582c-.032-.499.119-1.05.53-1.456l.815-.806c.081-.08.073-.159.059-.19a6.464 6.464 0 0 0-.573-.989c-.02-.03-.085-.076-.195-.046l-1.102.303c-.56.153-1.113.008-1.53-.27a4.44 4.44 0 0 0-.501-.29c-.447-.222-.85-.629-.997-1.189l-.289-1.105c-.029-.11-.101-.143-.137-.146a6.6 6.6 0 0 0-1.142 0ZM11 8a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM9.5 8a1.5 1.5 0 1 0-3.001.001A1.5 1.5 0 0 0 9.5 8Z"></path>
</svg>
        <span data-content="Settings">Settings</span>
          <span id="settings-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
</ul>
    <div style="visibility:hidden;" data-view-component="true" class="UnderlineNav-actions js-responsive-underlinenav-overflow position-absolute pr-3 pr-md-4 pr-lg-5 right-0">      <action-menu data-select-variant="none" data-view-component="true" data-catalyst="" data-ready="true">
  <focus-group direction="vertical" mnemonics="" retain="">
    <button id="action-menu-be1bbe40-c9c9-4566-8c7a-d285739fc6ad-button" popovertarget="action-menu-be1bbe40-c9c9-4566-8c7a-d285739fc6ad-overlay" aria-controls="action-menu-be1bbe40-c9c9-4566-8c7a-d285739fc6ad-list" aria-haspopup="true" aria-labelledby="tooltip-55f767cc-cbc2-4e51-a1ea-89e53e28cd22" type="button" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium UnderlineNav-item">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal Button-visual">
    <path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path>
</svg>
</button><tool-tip id="tooltip-55f767cc-cbc2-4e51-a1ea-89e53e28cd22" for="action-menu-be1bbe40-c9c9-4566-8c7a-d285739fc6ad-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Additional navigation options</tool-tip>


<anchored-position data-target="action-menu.overlay" id="action-menu-be1bbe40-c9c9-4566-8c7a-d285739fc6ad-overlay" anchor="action-menu-be1bbe40-c9c9-4566-8c7a-d285739fc6ad-button" align="start" side="outside-bottom" anchor-offset="normal" popover="auto" data-view-component="true" style="inset: 36px auto auto 0px;">
  <div data-view-component="true" class="Overlay Overlay--size-auto">
    
      <div data-view-component="true" class="Overlay-body Overlay-body--paddingNone">          <action-list data-catalyst="">
  <div data-view-component="true">
    <ul aria-labelledby="action-menu-be1bbe40-c9c9-4566-8c7a-d285739fc6ad-button" id="action-menu-be1bbe40-c9c9-4566-8c7a-d285739fc6ad-list" role="menu" data-view-component="true" class="ActionListWrap--inset ActionListWrap">
        <li hidden="" data-menu-item="i0code-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-26f6eccd-b41e-42f4-971e-f7a946aa8756" href="https://github.com/SharmilaShroff/image-processing.py" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Code
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i1issues-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-e0c5235c-176f-46b8-b77f-60d0636b7507" href="https://github.com/SharmilaShroff/image-processing.py/issues" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Issues
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i2pull-requests-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-5b5abbf6-28e2-451c-99ca-52e6298c19e7" href="https://github.com/SharmilaShroff/image-processing.py/pulls" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Pull requests
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i3actions-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-5c9ac124-1252-45fa-b68a-a6a74402d19a" href="https://github.com/SharmilaShroff/image-processing.py/actions" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Actions
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i4projects-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-b1d62267-8579-4d9b-b73a-90ebbabba181" href="https://github.com/SharmilaShroff/image-processing.py/projects" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Projects
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i5wiki-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-18cc04e1-3585-40a7-8f6a-c70d7123f179" href="https://github.com/SharmilaShroff/image-processing.py/wiki" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-book">
    <path d="M0 1.75A.75.75 0 0 1 .75 1h4.253c1.227 0 2.317.59 3 1.501A3.743 3.743 0 0 1 11.006 1h4.245a.75.75 0 0 1 .75.75v10.5a.75.75 0 0 1-.75.75h-4.507a2.25 2.25 0 0 0-1.591.659l-.622.621a.75.75 0 0 1-1.06 0l-.622-.621A2.25 2.25 0 0 0 5.258 13H.75a.75.75 0 0 1-.75-.75Zm7.251 10.324.004-5.073-.002-2.253A2.25 2.25 0 0 0 5.003 2.5H1.5v9h3.757a3.75 3.75 0 0 1 1.994.574ZM8.755 4.75l-.004 7.322a3.752 3.752 0 0 1 1.992-.572H14.5v-9h-3.495a2.25 2.25 0 0 0-2.25 2.25Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Wiki
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i6security-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-bb219df2-7c09-4567-9a83-b1587fad68b9" href="https://github.com/SharmilaShroff/image-processing.py/security" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-shield">
    <path d="M7.467.133a1.748 1.748 0 0 1 1.066 0l5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667Zm.61 1.429a.25.25 0 0 0-.153 0l-5.25 1.68a.25.25 0 0 0-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.196.196 0 0 0 .154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.251.251 0 0 0-.174-.237l-5.25-1.68ZM8.75 4.75v3a.75.75 0 0 1-1.5 0v-3a.75.75 0 0 1 1.5 0ZM9 10.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Security
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i7insights-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-11ada38e-e5b8-4a9c-af64-53710287e6b1" href="https://github.com/SharmilaShroff/image-processing.py/pulse" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-graph">
    <path d="M1.5 1.75V13.5h13.75a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1-.75-.75V1.75a.75.75 0 0 1 1.5 0Zm14.28 2.53-5.25 5.25a.75.75 0 0 1-1.06 0L7 7.06 4.28 9.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.25-3.25a.75.75 0 0 1 1.06 0L10 7.94l4.72-4.72a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Insights
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i8settings-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-fc42a7ab-fe9e-4390-a6b3-e661782d2182" href="https://github.com/SharmilaShroff/image-processing.py/settings" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-gear">
    <path d="M8 0a8.2 8.2 0 0 1 .701.031C9.444.095 9.99.645 10.16 1.29l.288 1.107c.018.066.079.158.212.224.231.114.454.243.668.386.123.082.233.09.299.071l1.103-.303c.644-.176 1.392.021 1.82.63.27.385.506.792.704 1.218.315.675.111 1.422-.364 1.891l-.814.806c-.049.048-.098.147-.088.294.016.257.016.515 0 .772-.01.147.038.246.088.294l.814.806c.475.469.679 1.216.364 1.891a7.977 7.977 0 0 1-.704 1.217c-.428.61-1.176.807-1.82.63l-1.102-.302c-.067-.019-.177-.011-.3.071a5.909 5.909 0 0 1-.668.386c-.133.066-.194.158-.211.224l-.29 1.106c-.168.646-.715 1.196-1.458 1.26a8.006 8.006 0 0 1-1.402 0c-.743-.064-1.289-.614-1.458-1.26l-.289-1.106c-.018-.066-.079-.158-.212-.224a5.738 5.738 0 0 1-.668-.386c-.123-.082-.233-.09-.299-.071l-1.103.303c-.644.176-1.392-.021-1.82-.63a8.12 8.12 0 0 1-.704-1.218c-.315-.675-.111-1.422.363-1.891l.815-.806c.05-.048.098-.147.088-.294a6.214 6.214 0 0 1 0-.772c.01-.147-.038-.246-.088-.294l-.815-.806C.635 6.045.431 5.298.746 4.623a7.92 7.92 0 0 1 .704-1.217c.428-.61 1.176-.807 1.82-.63l1.102.302c.067.019.177.011.3-.071.214-.143.437-.272.668-.386.133-.066.194-.158.211-.224l.29-1.106C6.009.645 6.556.095 7.299.03 7.53.01 7.764 0 8 0Zm-.571 1.525c-.036.003-.108.036-.137.146l-.289 1.105c-.147.561-.549.967-.998 1.189-.173.086-.34.183-.5.29-.417.278-.97.423-1.529.27l-1.103-.303c-.109-.03-.175.016-.195.045-.22.312-.412.644-.573.99-.014.031-.021.11.059.19l.815.806c.411.406.562.957.53 1.456a4.709 4.709 0 0 0 0 .582c.032.499-.119 1.05-.53 1.456l-.815.806c-.081.08-.073.159-.059.19.162.346.353.677.573.989.02.03.085.076.195.046l1.102-.303c.56-.153 1.113-.008 1.53.27.161.107.328.204.501.29.447.222.85.629.997 1.189l.289 1.105c.029.109.101.143.137.146a6.6 6.6 0 0 0 1.142 0c.036-.003.108-.036.137-.146l.289-1.105c.147-.561.549-.967.998-1.189.173-.086.34-.183.5-.29.417-.278.97-.423 1.529-.27l1.103.303c.109.029.175-.016.195-.045.22-.313.411-.644.573-.99.014-.031.021-.11-.059-.19l-.815-.806c-.411-.406-.562-.957-.53-1.456a4.709 4.709 0 0 0 0-.582c-.032-.499.119-1.05.53-1.456l.815-.806c.081-.08.073-.159.059-.19a6.464 6.464 0 0 0-.573-.989c-.02-.03-.085-.076-.195-.046l-1.102.303c-.56.153-1.113.008-1.53-.27a4.44 4.44 0 0 0-.501-.29c-.447-.222-.85-.629-.997-1.189l-.289-1.105c-.029-.11-.101-.143-.137-.146a6.6 6.6 0 0 0-1.142 0ZM11 8a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM9.5 8a1.5 1.5 0 1 0-3.001.001A1.5 1.5 0 0 0 9.5 8Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Settings
</span>      
</a>
  
</li>
</ul>    
</div></action-list>


</div>
      
</div></anchored-position>  </focus-group>
</action-menu></div>
</nav>
              
            </div>
    </header>


      <div hidden="hidden" data-view-component="true" class="js-stale-session-flash stale-session-flash flash flash-warn flash-full">
  
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span class="js-stale-session-flash-signed-in" hidden="">You signed in with another tab or window. <a class="Link--inTextBlock" href="https://github.com/SharmilaShroff/image-processing.py">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-signed-out" hidden="">You signed out in another tab or window. <a class="Link--inTextBlock" href="https://github.com/SharmilaShroff/image-processing.py">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-switched" hidden="">You switched accounts on another tab or window. <a class="Link--inTextBlock" href="https://github.com/SharmilaShroff/image-processing.py">Reload</a> to refresh your session.</span>

    <button id="icon-button-63721008-13bb-436f-9d94-2ad30b6e6646" aria-labelledby="tooltip-78993f95-b146-4e8f-9e98-3ebf601c5869" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium flash-close js-flash-close">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x Button-visual">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</button><tool-tip id="tooltip-78993f95-b146-4e8f-9e98-3ebf601c5869" for="icon-button-63721008-13bb-436f-9d94-2ad30b6e6646" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Dismiss alert</tool-tip>


  
</div>
        
          
    </div>

  <div id="start-of-content" class="show-on-focus"></div>








    <div id="js-flash-container" class="flash-container" data-turbo-replace="">


      


  <template class="js-flash-template"></template>
</div>


    
  <notification-shelf-watcher data-base-url="https://github.com/notifications/beta/shelf" data-channel="eyJjIjoibm90aWZpY2F0aW9uLWNoYW5nZWQ6MTkwMzU3NjM2IiwidCI6MTc2NzYyNDMwNH0=--0c4cec09e4a41eb94324b87582cbdb32bbc927973a982037a622a20255418989" data-view-component="true" class="js-socket-channel" data-refresh-delay="500" data-catalyst="" data-throttle-delay="5000"></notification-shelf-watcher>
  <div hidden="" data-initial="" data-target="notification-shelf-watcher.placeholder"></div>






  <div class="application-main " data-commit-hovercards-enabled="" data-discussion-hovercards-enabled="" data-issue-and-pr-hovercards-enabled="" data-project-hovercards-enabled="">
        <div itemscope="" itemtype="http://schema.org/SoftwareSourceCode" class="">
    <main id="js-repo-pjax-container">
      
  


<template class="js-user-list-create-dialog-template" data-label="Create list"></template>



    






  
    

  <div id="repository-container-header" class="pt-3 hide-full-screen" data-turbo-replace="">

      <div class="d-flex flex-nowrap flex-justify-end mb-3  container-xl  px-3 px-lg-5" style="gap: 1rem;">

        <div class="flex-auto min-width-0 width-fit">
              <div id="repo-title-component" class=" d-flex flex-nowrap flex-items-center wb-break-word f3 text-normal">
    <img class="avatar mr-2 d-none d-md-block avatar-user" alt="Owner avatar" src="./blue_filter_files/190357636(1)" width="24" height="24">
  

  <strong itemprop="name" class="mr-2 flex-self-stretch d-none d-md-block no-wrap overflow-x-hidden">
    <a data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" class="d-block overflow-x-hidden color-fg-default" style="text-overflow: ellipsis;" href="https://github.com/SharmilaShroff/image-processing.py">image-processing.py</a>
  </strong>

  <span></span><span class="Label Label--secondary v-align-middle mr-1 d-none d-md-block">Public</span>
</div>

<div class="d-none d-md-block">
</div>


        </div>

        <div id="repository-details-container" class="flex-shrink-0" data-turbo-replace="" style="max-width: 70%;">
            <ul class="pagehead-actions flex-shrink-0 d-none d-md-inline" style="padding: 2px 0;">
    
      <li>
  <div class="float-left">
    <!-- '"` --><!-- </textarea></xmp> --><form data-turbo="false" action="https://github.com/SharmilaShroff/image-processing.py/profile_pin" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="IUbfxKois4w_vs7tnjdT8ONd9fzwFgSLNJBXdyigKd7llb3CIbsRZG4MHc85xL095YAC7Ki-2sY_pKbZzAVWmg" autocomplete="off">
        <button title="Pin this repository to your profile" type="submit" data-view-component="true" class="btn-sm btn">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-pin mr-2">
    <path d="m11.294.984 3.722 3.722a1.75 1.75 0 0 1-.504 2.826l-1.327.613a3.089 3.089 0 0 0-1.707 2.084l-.584 2.454c-.317 1.332-1.972 1.8-2.94.832L5.75 11.311 1.78 15.28a.749.749 0 1 1-1.06-1.06l3.969-3.97-2.204-2.204c-.968-.968-.5-2.623.832-2.94l2.454-.584a3.08 3.08 0 0 0 2.084-1.707l.613-1.327a1.75 1.75 0 0 1 2.826-.504ZM6.283 9.723l2.732 2.731a.25.25 0 0 0 .42-.119l.584-2.454a4.586 4.586 0 0 1 2.537-3.098l1.328-.613a.25.25 0 0 0 .072-.404l-3.722-3.722a.25.25 0 0 0-.404.072l-.613 1.328a4.584 4.584 0 0 1-3.098 2.537l-2.454.584a.25.25 0 0 0-.119.42l2.731 2.732Z"></path>
</svg>Pin
</button></form>  </div>
</li>


  <li>
              <link crossorigin="anonymous" media="all" rel="stylesheet" href="./blue_filter_files/primer-react.47239ec6cbe68138fe4c.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./blue_filter_files/notifications-subscriptions-menu.933100a30c03fd4e8ae4.module.css">

<react-partial partial-name="notifications-subscriptions-menu" data-ssr="false" data-attempted-ssr="false" data-react-profiling="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"subscriptionType":"none","repositoryId":1098386497,"repositoryName":"SharmilaShroff/image-processing.py","watchersCount":0,"subscribableThreadTypes":[{"name":"Issue","enabled":true,"subscribed":false},{"name":"PullRequest","enabled":true,"subscribed":false},{"name":"Release","enabled":true,"subscribed":false},{"name":"Discussion","enabled":false,"subscribed":false},{"name":"SecurityAlert","enabled":true,"subscribed":false}],"repositoryLabels":[],"showLabelSubscriptions":false}}</script>
  <div data-target="react-partial.reactRoot"><div class="d-md-none"><button type="button" data-testid="notifications-subscriptions-menu-button-desktop" aria-label="Watch: Participating in SharmilaShroff/image-processing.py" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-9n-Xk NotificationsSubscriptionsMenu-module__watchButton--ccU5u" data-loading="false" data-size="medium" data-variant="default" id=":rq:"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-eye" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M8 2c1.981 0 3.671.992 4.933 2.078 1.27 1.091 2.187 2.345 2.637 3.023a1.62 1.62 0 0 1 0 1.798c-.45.678-1.367 1.932-2.637 3.023C11.67 13.008 9.981 14 8 14c-1.981 0-3.671-.992-4.933-2.078C1.797 10.83.88 9.576.43 8.898a1.62 1.62 0 0 1 0-1.798c.45-.677 1.367-1.931 2.637-3.022C4.33 2.992 6.019 2 8 2ZM1.679 7.932a.12.12 0 0 0 0 .136c.411.622 1.241 1.75 2.366 2.717C5.176 11.758 6.527 12.5 8 12.5c1.473 0 2.825-.742 3.955-1.715 1.124-.967 1.954-2.096 2.366-2.717a.12.12 0 0 0 0-.136c-.412-.621-1.242-1.75-2.366-2.717C10.824 4.242 9.473 3.5 8 3.5c-1.473 0-2.825.742-3.955 1.715-1.124.967-1.954 2.096-2.366 2.717ZM8 10a2 2 0 1 1-.001-3.999A2 2 0 0 1 8 10Z"></path></svg></span><span data-component="text" class="prc-Button-Label-FWkx3"></span></span></button></div><div class="d-none d-md-block"><button type="button" data-testid="notifications-subscriptions-menu-button-mobile" aria-label="Watch: Participating in SharmilaShroff/image-processing.py" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-9n-Xk NotificationsSubscriptionsMenu-module__ActionMenuButton--UgYy6" data-loading="false" data-size="small" data-variant="default" id=":rt:"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-eye" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M8 2c1.981 0 3.671.992 4.933 2.078 1.27 1.091 2.187 2.345 2.637 3.023a1.62 1.62 0 0 1 0 1.798c-.45.678-1.367 1.932-2.637 3.023C11.67 13.008 9.981 14 8 14c-1.981 0-3.671-.992-4.933-2.078C1.797 10.83.88 9.576.43 8.898a1.62 1.62 0 0 1 0-1.798c.45-.677 1.367-1.931 2.637-3.022C4.33 2.992 6.019 2 8 2ZM1.679 7.932a.12.12 0 0 0 0 .136c.411.622 1.241 1.75 2.366 2.717C5.176 11.758 6.527 12.5 8 12.5c1.473 0 2.825-.742 3.955-1.715 1.124-.967 1.954-2.096 2.366-2.717a.12.12 0 0 0 0-.136c-.412-.621-1.242-1.75-2.366-2.717C10.824 4.242 9.473 3.5 8 3.5c-1.473 0-2.825.742-3.955 1.715-1.124.967-1.954 2.096-2.366 2.717ZM8 10a2 2 0 1 1-.001-3.999A2 2 0 0 1 8 10Z"></path></svg></span><span data-component="text" class="prc-Button-Label-FWkx3">Watch<span class="ml-2 Counter rounded-3 NotificationsSubscriptionsMenu-module__watchCounter--vgIup">0</span></span></span><span data-component="trailingAction" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></button></div><script type="application/json" id="__PRIMER_DATA_:rp:__">{"resolvedServerColorMode":"day"}</script></div>
</react-partial>




  </li>

  <li>
        <div data-view-component="true" class="BtnGroup d-flex">
        <button icon="repo-forked" id="fork-button" aria-disabled="true" type="button" data-view-component="true" class="btn-sm btn BtnGroup-item" aria-describedby="tooltip-097525bd-9475-414f-a4bf-51bd606058f0">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo-forked mr-2">
    <path d="M5 5.372v.878c0 .414.336.75.75.75h4.5a.75.75 0 0 0 .75-.75v-.878a2.25 2.25 0 1 1 1.5 0v.878a2.25 2.25 0 0 1-2.25 2.25h-1.5v2.128a2.251 2.251 0 1 1-1.5 0V8.5h-1.5A2.25 2.25 0 0 1 3.5 6.25v-.878a2.25 2.25 0 1 1 1.5 0ZM5 3.25a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Zm6.75.75a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5Zm-3 8.75a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Z"></path>
</svg>Fork
        <span id="repo-network-counter" data-pjax-replace="true" data-turbo-replace="true" title="0" data-view-component="true" class="Counter">0</span>
        <tool-tip id="tooltip-097525bd-9475-414f-a4bf-51bd606058f0" for="fork-button" popover="manual" data-direction="s" data-type="description" data-view-component="true" class="sr-only position-absolute" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Cannot fork because you own this repository and are not a member of any organizations.</tool-tip>
</button>
      <details group_item="true" id="my-forks-menu-1098386497" data-view-component="true" class="details-reset details-overlay BtnGroup-parent d-inline-block position-relative">
              <summary aria-label="See your forks of this repository" data-view-component="true" class="btn-sm btn BtnGroup-item px-2 float-none" aria-haspopup="menu" role="button">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-triangle-down">
    <path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path>
</svg>
</summary>
  <details-menu class="SelectMenu right-0" src="/SharmilaShroff/image-processing.py/my_forks_menu_content?can_fork=false" role="menu">
    <div class="SelectMenu-modal">
        <button class="SelectMenu-closeButton position-absolute right-0 m-2" type="button" aria-label="Close menu" data-toggle-for="my-forks-menu-1098386497">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        </button>
      <div id="filter-menu-1bca96" class="d-flex flex-column flex-1 overflow-hidden">
        <div class="SelectMenu-list">

            <include-fragment aria-label="Loading" data-nonce="v2:2b815f31-74b1-a9f7-c69b-a73f6467a217" data-view-component="true" class="SelectMenu-loading"><template shadowrootmode="open"><style>:host {display: block;}</style><slot></slot></template>
  
                <p data-show-on-error="" hidden="">
                  Forks could not be loaded
                </p>
                <span data-hide-on-error="">
              <span data-view-component="true">
  <svg role="menuitem" style="box-sizing: content-box; color: var(--color-icon-primary);" width="32" height="32" viewBox="0 0 16 16" fill="none" aria-hidden="true" data-view-component="true" class="anim-rotate">
    <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none"></circle>
    <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>    <span class="sr-only">Loading</span>
</span>
                </span>

  <div data-show-on-forbidden-error="" hidden="">
    <div class="Box">
  <div class="blankslate-container">
    <div data-view-component="true" class="blankslate blankslate-spacious color-bg-default rounded-2">
      

      <h3 data-view-component="true" class="blankslate-heading">        Uh oh!
</h3>
      <p data-view-component="true">        </p><p class="color-fg-muted my-2 mb-2 ws-normal">There was an error while loading. <a class="Link--inTextBlock" data-turbo="false" href="https://github.com/SharmilaShroff/image-processing.py" aria-label="Please reload this page">Please reload this page</a>.</p>
<p></p>

</div>  </div>
</div>  </div>
</include-fragment>        </div>
        
      </div>
    </div>
  </details-menu>
</details></div>
  </li>

  <li>
        <template class="js-unstar-confirmation-dialog-template" aria-live="polite"></template>

  <div data-view-component="true" class="js-toggler-container js-social-container starring-container d-flex">
    <div data-view-component="true" class="starred BtnGroup flex-1 ml-0">
      <!-- '"` --><!-- </textarea></xmp> --><form class="js-social-form BtnGroup-parent flex-auto js-deferred-toggler-target" data-turbo="false" action="https://github.com/SharmilaShroff/image-processing.py/unstar" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="zLFYNCAjPT97WXqL9Poh2H0MpC5kk9pEX8vwthQfFZw3IcRm0Ltjd0zZrGC7J47vTESU5YmjjpC9LoJQ8pcWBw" autocomplete="off">
          <input type="hidden" value="h4-XJkQ17E2fkKmcRhIBEdZza3E6U2cd0LBM0X4olQN8Hwt0tK2yBagQf3cJz64m5ztbutdjM8kyVT43mKCWmA" data-csrf="true" class="js-confirm-csrf-token">
        <input type="hidden" name="context" value="repository">
          <button data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;UNSTAR_BUTTON&quot;,&quot;repository_id&quot;:1098386497,&quot;originating_url&quot;:&quot;https://github.com/SharmilaShroff/image-processing.py&quot;,&quot;user_id&quot;:190357636}}" data-hydro-click-hmac="1589957e97fe3a48e47e9a3b9ad4df1c675e553205b0d38dfc7299d038187a16" data-ga-click="Repository, click unstar button, action:files#disambiguate; text:Unstar" data-aria-prefix="Starred, click to unstar this repository" aria-label="Starred, click to unstar this repository (0)" type="submit" data-view-component="true" class="rounded-left-2 btn-with-aria-count btn-sm btn BtnGroup-item">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star-fill starred-button-icon d-inline-block mr-2">
    <path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Z"></path>
</svg><span data-view-component="true" class="d-inline">
              Starred
</span>              <span id="repo-stars-counter-unstar" aria-label="0 users starred this repository" data-singular-suffix="user starred this repository" data-plural-suffix="users starred this repository" data-turbo-replace="true" title="0" data-view-component="true" class="Counter js-social-count">0</span>
</button></form>          <details id="details-user-list-1098386497-starred" data-view-component="true" class="details-reset details-overlay BtnGroup-parent js-user-list-menu d-flex position-relative">
          <summary aria-label="Add this repository to a list" data-view-component="true" class="btn-sm btn BtnGroup-item px-2 float-none" aria-haspopup="menu" role="button">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-triangle-down">
    <path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path>
</svg>
</summary>
  <details-menu class="SelectMenu right-0" src="/SharmilaShroff/image-processing.py/lists" role="menu">
    <div class="SelectMenu-modal">
        <header class="SelectMenu-header">
                  <h4 class="SelectMenu-title f5" id="user-lists-menu">Lists</h4>

          <button class="SelectMenu-closeButton" type="button" aria-label="Close menu" data-toggle-for="details-user-list-1098386497-starred">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
          </button>
        </header>
      <div id="filter-menu-33a24f" class="d-flex flex-column flex-1 overflow-hidden">
        <div class="SelectMenu-list">

            <include-fragment aria-label="Loading" data-nonce="v2:2b815f31-74b1-a9f7-c69b-a73f6467a217" data-view-component="true" class="SelectMenu-loading"><template shadowrootmode="open"><style>:host {display: block;}</style><slot></slot></template>
  
              <span data-view-component="true">
  <svg role="menuitem" style="box-sizing: content-box; color: var(--color-icon-primary);" width="32" height="32" viewBox="0 0 16 16" fill="none" aria-hidden="true" data-view-component="true" class="anim-rotate">
    <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none"></circle>
    <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>    <span class="sr-only">Loading</span>
</span>

  <div data-show-on-forbidden-error="" hidden="">
    <div class="Box">
  <div class="blankslate-container">
    <div data-view-component="true" class="blankslate blankslate-spacious color-bg-default rounded-2">
      

      <h3 data-view-component="true" class="blankslate-heading">        Uh oh!
</h3>
      <p data-view-component="true">        </p><p class="color-fg-muted my-2 mb-2 ws-normal">There was an error while loading. <a class="Link--inTextBlock" data-turbo="false" href="https://github.com/SharmilaShroff/image-processing.py" aria-label="Please reload this page">Please reload this page</a>.</p>
<p></p>

</div>  </div>
</div>  </div>
</include-fragment>        </div>
        
      </div>
    </div>
  </details-menu>
</details>
</div>
    <div data-view-component="true" class="unstarred BtnGroup ml-0 flex-1">
      <!-- '"` --><!-- </textarea></xmp> --><form class="js-social-form BtnGroup-parent flex-auto" data-turbo="false" action="https://github.com/SharmilaShroff/image-processing.py/star" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="JBvhIMTqCzt_6dGggYxNNJwoRBsRATEUbRDmj21ZVAl3JsIVv0gqK6lbNZAveKjy6fkn_JwGDiYtlIoeqeAriw" autocomplete="off">
        <input type="hidden" name="context" value="repository">
          <button data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;STAR_BUTTON&quot;,&quot;repository_id&quot;:1098386497,&quot;originating_url&quot;:&quot;https://github.com/SharmilaShroff/image-processing.py&quot;,&quot;user_id&quot;:190357636}}" data-hydro-click-hmac="a60ce1dc779939019ec742c99842075172613ef8a83c75ebd7970273a46dba04" data-ga-click="Repository, click star button, action:files#disambiguate; text:Star" data-aria-prefix="Star this repository" aria-label="Star this repository (0)" type="submit" data-view-component="true" class="js-toggler-target rounded-left-2 btn-with-aria-count btn-sm btn BtnGroup-item">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star d-inline-block mr-2">
    <path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Zm0 2.445L6.615 5.5a.75.75 0 0 1-.564.41l-3.097.45 2.24 2.184a.75.75 0 0 1 .216.664l-.528 3.084 2.769-1.456a.75.75 0 0 1 .698 0l2.77 1.456-.53-3.084a.75.75 0 0 1 .216-.664l2.24-2.183-3.096-.45a.75.75 0 0 1-.564-.41L8 2.694Z"></path>
</svg><span data-view-component="true" class="d-inline">
              Star
</span>              <span id="repo-stars-counter-star" aria-label="0 users starred this repository" data-singular-suffix="user starred this repository" data-plural-suffix="users starred this repository" data-turbo-replace="true" title="0" data-view-component="true" class="Counter js-social-count">0</span>
</button></form>          <details id="details-user-list-1098386497-unstarred" data-view-component="true" class="details-reset details-overlay BtnGroup-parent js-user-list-menu d-flex position-relative">
          <summary aria-label="Add this repository to a list" data-view-component="true" class="btn-sm btn BtnGroup-item px-2 float-none" aria-haspopup="menu" role="button">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-triangle-down">
    <path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path>
</svg>
</summary>
  <details-menu class="SelectMenu right-0" src="/SharmilaShroff/image-processing.py/lists" role="menu">
    <div class="SelectMenu-modal">
        <header class="SelectMenu-header">
                  <h4 class="SelectMenu-title f5" id="user-lists-menu">Lists</h4>

          <button class="SelectMenu-closeButton" type="button" aria-label="Close menu" data-toggle-for="details-user-list-1098386497-unstarred">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
          </button>
        </header>
      <div id="filter-menu-cb9766" class="d-flex flex-column flex-1 overflow-hidden">
        <div class="SelectMenu-list">

            <include-fragment aria-label="Loading" data-nonce="v2:2b815f31-74b1-a9f7-c69b-a73f6467a217" data-view-component="true" class="SelectMenu-loading"><template shadowrootmode="open"><style>:host {display: block;}</style><slot></slot></template>
  
              <span data-view-component="true">
  <svg role="menuitem" style="box-sizing: content-box; color: var(--color-icon-primary);" width="32" height="32" viewBox="0 0 16 16" fill="none" aria-hidden="true" data-view-component="true" class="anim-rotate">
    <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none"></circle>
    <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>    <span class="sr-only">Loading</span>
</span>

  <div data-show-on-forbidden-error="" hidden="">
    <div class="Box">
  <div class="blankslate-container">
    <div data-view-component="true" class="blankslate blankslate-spacious color-bg-default rounded-2">
      

      <h3 data-view-component="true" class="blankslate-heading">        Uh oh!
</h3>
      <p data-view-component="true">        </p><p class="color-fg-muted my-2 mb-2 ws-normal">There was an error while loading. <a class="Link--inTextBlock" data-turbo="false" href="https://github.com/SharmilaShroff/image-processing.py" aria-label="Please reload this page">Please reload this page</a>.</p>
<p></p>

</div>  </div>
</div>  </div>
</include-fragment>        </div>
        
      </div>
    </div>
  </details-menu>
</details>
</div></div>
  </li>

</ul>

        </div>
      </div>

        <div class=" container-xl ">
          <div id="responsive-meta-container" data-turbo-replace="">
      <div class="d-block d-md-none mb-2 px-3 px-md-4 px-lg-5">
        <div class="d-flex gap-2 mt-n3 mb-3 flex-wrap">
          <div class="d-flex flex-row gap-2">
                <link crossorigin="anonymous" media="all" rel="stylesheet" href="./blue_filter_files/primer-react.47239ec6cbe68138fe4c.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./blue_filter_files/notifications-subscriptions-menu.933100a30c03fd4e8ae4.module.css">

<react-partial partial-name="notifications-subscriptions-menu" data-ssr="false" data-attempted-ssr="false" data-react-profiling="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"subscriptionType":"none","repositoryId":1098386497,"repositoryName":"SharmilaShroff/image-processing.py","watchersCount":0,"subscribableThreadTypes":[{"name":"Issue","enabled":true,"subscribed":false},{"name":"PullRequest","enabled":true,"subscribed":false},{"name":"Release","enabled":true,"subscribed":false},{"name":"Discussion","enabled":false,"subscribed":false},{"name":"SecurityAlert","enabled":true,"subscribed":false}],"repositoryLabels":[],"showLabelSubscriptions":false}}</script>
  <div data-target="react-partial.reactRoot"><div class="d-md-none"><button type="button" data-testid="notifications-subscriptions-menu-button-desktop" aria-label="Watch: Participating in SharmilaShroff/image-processing.py" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-9n-Xk NotificationsSubscriptionsMenu-module__watchButton--ccU5u" data-loading="false" data-size="medium" data-variant="default" id=":r3:"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-eye" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M8 2c1.981 0 3.671.992 4.933 2.078 1.27 1.091 2.187 2.345 2.637 3.023a1.62 1.62 0 0 1 0 1.798c-.45.678-1.367 1.932-2.637 3.023C11.67 13.008 9.981 14 8 14c-1.981 0-3.671-.992-4.933-2.078C1.797 10.83.88 9.576.43 8.898a1.62 1.62 0 0 1 0-1.798c.45-.677 1.367-1.931 2.637-3.022C4.33 2.992 6.019 2 8 2ZM1.679 7.932a.12.12 0 0 0 0 .136c.411.622 1.241 1.75 2.366 2.717C5.176 11.758 6.527 12.5 8 12.5c1.473 0 2.825-.742 3.955-1.715 1.124-.967 1.954-2.096 2.366-2.717a.12.12 0 0 0 0-.136c-.412-.621-1.242-1.75-2.366-2.717C10.824 4.242 9.473 3.5 8 3.5c-1.473 0-2.825.742-3.955 1.715-1.124.967-1.954 2.096-2.366 2.717ZM8 10a2 2 0 1 1-.001-3.999A2 2 0 0 1 8 10Z"></path></svg></span><span data-component="text" class="prc-Button-Label-FWkx3"></span></span></button></div><div class="d-none d-md-block"><button type="button" data-testid="notifications-subscriptions-menu-button-mobile" aria-label="Watch: Participating in SharmilaShroff/image-processing.py" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-9n-Xk NotificationsSubscriptionsMenu-module__ActionMenuButton--UgYy6" data-loading="false" data-size="small" data-variant="default" id=":r6:"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-eye" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M8 2c1.981 0 3.671.992 4.933 2.078 1.27 1.091 2.187 2.345 2.637 3.023a1.62 1.62 0 0 1 0 1.798c-.45.678-1.367 1.932-2.637 3.023C11.67 13.008 9.981 14 8 14c-1.981 0-3.671-.992-4.933-2.078C1.797 10.83.88 9.576.43 8.898a1.62 1.62 0 0 1 0-1.798c.45-.677 1.367-1.931 2.637-3.022C4.33 2.992 6.019 2 8 2ZM1.679 7.932a.12.12 0 0 0 0 .136c.411.622 1.241 1.75 2.366 2.717C5.176 11.758 6.527 12.5 8 12.5c1.473 0 2.825-.742 3.955-1.715 1.124-.967 1.954-2.096 2.366-2.717a.12.12 0 0 0 0-.136c-.412-.621-1.242-1.75-2.366-2.717C10.824 4.242 9.473 3.5 8 3.5c-1.473 0-2.825.742-3.955 1.715-1.124.967-1.954 2.096-2.366 2.717ZM8 10a2 2 0 1 1-.001-3.999A2 2 0 0 1 8 10Z"></path></svg></span><span data-component="text" class="prc-Button-Label-FWkx3">Watch<span class="ml-2 Counter rounded-3 NotificationsSubscriptionsMenu-module__watchCounter--vgIup">0</span></span></span><span data-component="trailingAction" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></button></div><script type="application/json" id="__PRIMER_DATA_:r2:__">{"resolvedServerColorMode":"day"}</script></div>
</react-partial>



              <div data-view-component="true" class="BtnGroup d-flex">
      <a id="fork-icon-button" variant="small" group_item="true" href="https://github.com/SharmilaShroff/image-processing.py/fork" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;FORK_BUTTON&quot;,&quot;repository_id&quot;:1098386497,&quot;originating_url&quot;:&quot;https://github.com/SharmilaShroff/image-processing.py&quot;,&quot;user_id&quot;:190357636}}" data-hydro-click-hmac="0dbc12bb75b6e0f2a45fa219a41c879a75d5fd62221ba62b30eba96a8c4b30c6" data-ga-click="Repository, show fork modal, action:files#disambiguate; text:Fork" aria-labelledby="tooltip-42290fc7-05e2-4315-8175-bdb258d5fa69" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo-forked Button-visual">
    <path d="M5 5.372v.878c0 .414.336.75.75.75h4.5a.75.75 0 0 0 .75-.75v-.878a2.25 2.25 0 1 1 1.5 0v.878a2.25 2.25 0 0 1-2.25 2.25h-1.5v2.128a2.251 2.251 0 1 1-1.5 0V8.5h-1.5A2.25 2.25 0 0 1 3.5 6.25v-.878a2.25 2.25 0 1 1 1.5 0ZM5 3.25a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Zm6.75.75a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5Zm-3 8.75a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Z"></path>
</svg>
</a><tool-tip id="tooltip-42290fc7-05e2-4315-8175-bdb258d5fa69" for="fork-icon-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Fork your own copy of SharmilaShroff/image-processing.py</tool-tip>

</div>
              <style>
  /*
    This is kind of gross but let me explain.
    The triangle-down icon in the user lists menu component needs to be larger on small screens
    but Primer doesn't accept a responsive value for size.
    So instead we use CSS to override the size on small screens only, to match the ⭐ button beside it.
    The selector is written this way to avoid affecting other buttons inside the lists dropdown.
  */
  @media (max-width: 767px) {
    .icon-button-group .BtnGroup-parent > * > button:first-child {
      height: var(--control-medium-size);
      width: var(--control-medium-size);
      min-width: var(--control-medium-size);
    }
  }

  /* No idea what this is though. It was like this when I got here. */
  @media (min-width: 544px) {
    .icon-button-group .SelectMenu {
      right: auto !important;
      left: 0 !important;
    }
  }
</style>
  <div data-view-component="true" class="js-toggler-container starring-container">
    <div data-view-component="true" class="starred BtnGroup icon-button-group flex-1 ml-0">
      <!-- '"` --><!-- </textarea></xmp> --><form class="js-social-form BtnGroup-parent" data-turbo="false" action="https://github.com/SharmilaShroff/image-processing.py/unstar" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="nyNKNBDWtCcLdgwhW_VLP27ZwMhgmciOvN98j--yqnBks9Zm4E7qbzz22soUKOQIX5HwA42pnFpeOg5pCTqp6w" autocomplete="off">
        <input type="hidden" name="context" value="repository">
        <button data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;UNSTAR_BUTTON&quot;,&quot;repository_id&quot;:1098386497,&quot;originating_url&quot;:&quot;https://github.com/SharmilaShroff/image-processing.py&quot;,&quot;user_id&quot;:190357636}}" data-hydro-click-hmac="1589957e97fe3a48e47e9a3b9ad4df1c675e553205b0d38dfc7299d038187a16" data-ga-click="Repository, click unstar button, action:files#disambiguate; text:Unstar" id="icon-button-f7672981-f06b-463d-9b76-7c893662a43a" aria-labelledby="tooltip-00c5c330-e0d9-4466-bbf6-d6985df262fa" type="submit" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium js-toggler-target starred-button-icon BtnGroup-item rounded-left-2">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star-fill Button-visual">
    <path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Z"></path>
</svg>
</button><tool-tip id="tooltip-00c5c330-e0d9-4466-bbf6-d6985df262fa" for="icon-button-f7672981-f06b-463d-9b76-7c893662a43a" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Unstar this repository</tool-tip>

</form>          <details id="details-user-list-1098386497" data-view-component="true" class="details-reset details-overlay BtnGroup-parent js-user-list-menu d-flex position-relative">
          <summary aria-label="Add this repository to a list" data-view-component="true" class="btn-sm btn BtnGroup-item px-2 float-none" aria-haspopup="menu" role="button">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-triangle-down">
    <path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path>
</svg>
</summary>
  <details-menu class="SelectMenu right-0" src="/SharmilaShroff/image-processing.py/lists" role="menu">
    <div class="SelectMenu-modal">
        <header class="SelectMenu-header">
                  <h4 class="SelectMenu-title f5" id="user-lists-menu">Lists</h4>

          <button class="SelectMenu-closeButton" type="button" aria-label="Close menu" data-toggle-for="details-user-list-1098386497">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
          </button>
        </header>
      <div id="filter-menu-f10580" class="d-flex flex-column flex-1 overflow-hidden">
        <div class="SelectMenu-list">

            <include-fragment aria-label="Loading" data-nonce="v2:2b815f31-74b1-a9f7-c69b-a73f6467a217" data-view-component="true" class="SelectMenu-loading"><template shadowrootmode="open"><style>:host {display: block;}</style><slot></slot></template>
  
              <span data-view-component="true">
  <svg role="menuitem" style="box-sizing: content-box; color: var(--color-icon-primary);" width="32" height="32" viewBox="0 0 16 16" fill="none" aria-hidden="true" data-view-component="true" class="anim-rotate">
    <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none"></circle>
    <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>    <span class="sr-only">Loading</span>
</span>

  <div data-show-on-forbidden-error="" hidden="">
    <div class="Box">
  <div class="blankslate-container">
    <div data-view-component="true" class="blankslate blankslate-spacious color-bg-default rounded-2">
      

      <h3 data-view-component="true" class="blankslate-heading">        Uh oh!
</h3>
      <p data-view-component="true">        </p><p class="color-fg-muted my-2 mb-2 ws-normal">There was an error while loading. <a class="Link--inTextBlock" data-turbo="false" href="https://github.com/SharmilaShroff/image-processing.py" aria-label="Please reload this page">Please reload this page</a>.</p>
<p></p>

</div>  </div>
</div>  </div>
</include-fragment>        </div>
        
      </div>
    </div>
  </details-menu>
</details>
</div>
    <div data-view-component="true" class="unstarred BtnGroup icon-button-group flex-1 ml-0">
      <!-- '"` --><!-- </textarea></xmp> --><form class="js-social-form BtnGroup-parent" data-turbo="false" action="https://github.com/SharmilaShroff/image-processing.py/star" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="IormcXgLIC0pOW65kBKOGOiHFAAYY9IO4R81VozUPudxt8VEA6kBPf-Liok-5mvenVZ355Vk7Tyhm1nHSG1BZQ" autocomplete="off">
        <input type="hidden" name="context" value="repository">
        <button data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;STAR_BUTTON&quot;,&quot;repository_id&quot;:1098386497,&quot;originating_url&quot;:&quot;https://github.com/SharmilaShroff/image-processing.py&quot;,&quot;user_id&quot;:190357636}}" data-hydro-click-hmac="a60ce1dc779939019ec742c99842075172613ef8a83c75ebd7970273a46dba04" data-ga-click="Repository, click star button, action:files#disambiguate; text:Star" id="icon-button-635132a2-c9c7-4427-b83b-257b03b65968" aria-labelledby="tooltip-accde6e0-8958-40b5-adb3-be4765f1b9bd" type="submit" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium js-toggler-target BtnGroup-item rounded-left-2">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star Button-visual">
    <path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Zm0 2.445L6.615 5.5a.75.75 0 0 1-.564.41l-3.097.45 2.24 2.184a.75.75 0 0 1 .216.664l-.528 3.084 2.769-1.456a.75.75 0 0 1 .698 0l2.77 1.456-.53-3.084a.75.75 0 0 1 .216-.664l2.24-2.183-3.096-.45a.75.75 0 0 1-.564-.41L8 2.694Z"></path>
</svg>
</button><tool-tip id="tooltip-accde6e0-8958-40b5-adb3-be4765f1b9bd" for="icon-button-635132a2-c9c7-4427-b83b-257b03b65968" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Star this repository</tool-tip>

</form>          <details id="details-user-list-1098386497" data-view-component="true" class="details-reset details-overlay BtnGroup-parent js-user-list-menu d-flex position-relative">
          <summary aria-label="Add this repository to a list" data-view-component="true" class="btn-sm btn BtnGroup-item px-2 float-none" aria-haspopup="menu" role="button">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-triangle-down">
    <path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path>
</svg>
</summary>
  <details-menu class="SelectMenu right-0" src="/SharmilaShroff/image-processing.py/lists" role="menu">
    <div class="SelectMenu-modal">
        <header class="SelectMenu-header">
                  <h4 class="SelectMenu-title f5" id="user-lists-menu">Lists</h4>

          <button class="SelectMenu-closeButton" type="button" aria-label="Close menu" data-toggle-for="details-user-list-1098386497">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
          </button>
        </header>
      <div id="filter-menu-891508" class="d-flex flex-column flex-1 overflow-hidden">
        <div class="SelectMenu-list">

            <include-fragment aria-label="Loading" data-nonce="v2:2b815f31-74b1-a9f7-c69b-a73f6467a217" data-view-component="true" class="SelectMenu-loading"><template shadowrootmode="open"><style>:host {display: block;}</style><slot></slot></template>
  
              <span data-view-component="true">
  <svg role="menuitem" style="box-sizing: content-box; color: var(--color-icon-primary);" width="32" height="32" viewBox="0 0 16 16" fill="none" aria-hidden="true" data-view-component="true" class="anim-rotate">
    <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none"></circle>
    <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>    <span class="sr-only">Loading</span>
</span>

  <div data-show-on-forbidden-error="" hidden="">
    <div class="Box">
  <div class="blankslate-container">
    <div data-view-component="true" class="blankslate blankslate-spacious color-bg-default rounded-2">
      

      <h3 data-view-component="true" class="blankslate-heading">        Uh oh!
</h3>
      <p data-view-component="true">        </p><p class="color-fg-muted my-2 mb-2 ws-normal">There was an error while loading. <a class="Link--inTextBlock" data-turbo="false" href="https://github.com/SharmilaShroff/image-processing.py" aria-label="Please reload this page">Please reload this page</a>.</p>
<p></p>

</div>  </div>
</div>  </div>
</include-fragment>        </div>
        
      </div>
    </div>
  </details-menu>
</details>
</div></div>
          </div>
          <div class="d-flex flex-row gap-2">
            

          </div>
        </div>
      <p class="f4 mb-3 color-fg-muted">
        A Python script that loads an image, applies a strong box blur using Pillow (PIL), and displays the blurred output with Matplotlib.
      </p>

    

    <div class="mb-3">
        


<ul class="d-flex flex-wrap mb-2 gap-2" aria-label="Repository details">
  <a class="Link--secondary no-underline d-block mr-2" role="listitem" href="https://github.com/SharmilaShroff/image-processing.py/stargazers">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star mr-1">
    <path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Zm0 2.445L6.615 5.5a.75.75 0 0 1-.564.41l-3.097.45 2.24 2.184a.75.75 0 0 1 .216.664l-.528 3.084 2.769-1.456a.75.75 0 0 1 .698 0l2.77 1.456-.53-3.084a.75.75 0 0 1 .216-.664l2.24-2.183-3.096-.45a.75.75 0 0 1-.564-.41L8 2.694Z"></path>
</svg>
    <span class="text-bold color-fg-default">0</span>
    stars
</a>  <a class="Link--secondary no-underline d-block mr-2" role="listitem" href="https://github.com/SharmilaShroff/image-processing.py/forks">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo-forked mr-1">
    <path d="M5 5.372v.878c0 .414.336.75.75.75h4.5a.75.75 0 0 0 .75-.75v-.878a2.25 2.25 0 1 1 1.5 0v.878a2.25 2.25 0 0 1-2.25 2.25h-1.5v2.128a2.251 2.251 0 1 1-1.5 0V8.5h-1.5A2.25 2.25 0 0 1 3.5 6.25v-.878a2.25 2.25 0 1 1 1.5 0ZM5 3.25a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Zm6.75.75a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5Zm-3 8.75a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Z"></path>
</svg>
    <span class="text-bold color-fg-default">0</span>
    forks
</a>  <a class="Link--secondary no-underline d-block mr-2" role="listitem" href="https://github.com/SharmilaShroff/image-processing.py/watchers">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-eye mr-1">
    <path d="M8 2c1.981 0 3.671.992 4.933 2.078 1.27 1.091 2.187 2.345 2.637 3.023a1.62 1.62 0 0 1 0 1.798c-.45.678-1.367 1.932-2.637 3.023C11.67 13.008 9.981 14 8 14c-1.981 0-3.671-.992-4.933-2.078C1.797 10.83.88 9.576.43 8.898a1.62 1.62 0 0 1 0-1.798c.45-.677 1.367-1.931 2.637-3.022C4.33 2.992 6.019 2 8 2ZM1.679 7.932a.12.12 0 0 0 0 .136c.411.622 1.241 1.75 2.366 2.717C5.176 11.758 6.527 12.5 8 12.5c1.473 0 2.825-.742 3.955-1.715 1.124-.967 1.954-2.096 2.366-2.717a.12.12 0 0 0 0-.136c-.412-.621-1.242-1.75-2.366-2.717C10.824 4.242 9.473 3.5 8 3.5c-1.473 0-2.825.742-3.955 1.715-1.124.967-1.954 2.096-2.366 2.717ZM8 10a2 2 0 1 1-.001-3.999A2 2 0 0 1 8 10Z"></path>
</svg>
    <span class="text-bold color-fg-default">0</span>
    watching
</a>  <include-fragment loading="lazy" src="/SharmilaShroff/image-processing.py/branch-and-tag-count" data-nonce="v2:2b815f31-74b1-a9f7-c69b-a73f6467a217" data-view-component="true"><template shadowrootmode="open"><style>:host {display: block;}</style><slot></slot></template>
  
    <a class="Link--secondary no-underline d-block mr-2" role="listitem" href="https://github.com/SharmilaShroff/image-processing.py/branches">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-branch mr-1">
    <path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path>
</svg>
    <span class="color-fg-muted">Branches</span>
</a><a class="Link--secondary no-underline d-block mr-2" role="listitem" href="https://github.com/SharmilaShroff/image-processing.py/tags">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-tag mr-1">
    <path d="M1 7.775V2.75C1 1.784 1.784 1 2.75 1h5.025c.464 0 .91.184 1.238.513l6.25 6.25a1.75 1.75 0 0 1 0 2.474l-5.026 5.026a1.75 1.75 0 0 1-2.474 0l-6.25-6.25A1.752 1.752 0 0 1 1 7.775Zm1.5 0c0 .066.026.13.073.177l6.25 6.25a.25.25 0 0 0 .354 0l5.025-5.025a.25.25 0 0 0 0-.354l-6.25-6.25a.25.25 0 0 0-.177-.073H2.75a.25.25 0 0 0-.25.25ZM6 5a1 1 0 1 1 0 2 1 1 0 0 1 0-2Z"></path>
</svg>
    <span class="color-fg-muted">Tags</span>
</a>

  <div data-show-on-forbidden-error="" hidden="">
    <div class="Box">
  <div class="blankslate-container">
    <div data-view-component="true" class="blankslate blankslate-spacious color-bg-default rounded-2">
      

      <h3 data-view-component="true" class="blankslate-heading">        Uh oh!
</h3>
      <p data-view-component="true">        </p><p class="color-fg-muted my-2 mb-2 ws-normal">There was an error while loading. <a class="Link--inTextBlock" data-turbo="false" href="https://github.com/SharmilaShroff/image-processing.py" aria-label="Please reload this page">Please reload this page</a>.</p>
<p></p>

</div>  </div>
</div>  </div>
</include-fragment>  <a class="Link--secondary no-underline d-block mr-2" role="listitem" href="https://github.com/SharmilaShroff/image-processing.py/activity">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-pulse mr-1">
    <path d="M6 2c.306 0 .582.187.696.471L10 10.731l1.304-3.26A.751.751 0 0 1 12 7h3.25a.75.75 0 0 1 0 1.5h-2.742l-1.812 4.528a.751.751 0 0 1-1.392 0L6 4.77 4.696 8.03A.75.75 0 0 1 4 8.5H.75a.75.75 0 0 1 0-1.5h2.742l1.812-4.529A.751.751 0 0 1 6 2Z"></path>
</svg>
    <span>Activity</span>
</a>
</ul>

<div class="mb-2 d-flex color-fg-muted">
  <div class="d-flex flex-items-center" style="height: 21px">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-globe flex-shrink-0 mr-2">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM5.78 8.75a9.64 9.64 0 0 0 1.363 4.177c.255.426.542.832.857 1.215.245-.296.551-.705.857-1.215A9.64 9.64 0 0 0 10.22 8.75Zm4.44-1.5a9.64 9.64 0 0 0-1.363-4.177c-.307-.51-.612-.919-.857-1.215a9.927 9.927 0 0 0-.857 1.215A9.64 9.64 0 0 0 5.78 7.25Zm-5.944 1.5H1.543a6.507 6.507 0 0 0 4.666 5.5c-.123-.181-.24-.365-.352-.552-.715-1.192-1.437-2.874-1.581-4.948Zm-2.733-1.5h2.733c.144-2.074.866-3.756 1.58-4.948.12-.197.237-.381.353-.552a6.507 6.507 0 0 0-4.666 5.5Zm10.181 1.5c-.144 2.074-.866 3.756-1.58 4.948-.12.197-.237.381-.353.552a6.507 6.507 0 0 0 4.666-5.5Zm2.733-1.5a6.507 6.507 0 0 0-4.666-5.5c.123.181.24.365.353.552.714 1.192 1.436 2.874 1.58 4.948Z"></path>
</svg>
  </div>
  <span class="flex-auto min-width-0 width-fit">
    Public repository
  </span>
</div>

    </div>
  </div>

</div>

          <div class="border-bottom  mx-xl-5 "></div>
        </div>

  </div>



<turbo-frame id="repo-content-turbo-frame" target="_top" data-turbo-action="advance" class="">
    <div id="repo-content-pjax-container" class="repository-content ">
      <a href="https://github.dev/" class="d-none js-github-dev-shortcut" data-hotkey=".,Mod+Alt+.">Open in github.dev</a>
  <a href="https://github.dev/" class="d-none js-github-dev-new-tab-shortcut" data-hotkey="Shift+.,Shift+&gt;,&gt;" target="_blank" rel="noopener noreferrer">Open in a new github.dev tab</a>
    <a class="d-none" data-hotkey=",,Mod+Alt+," target="_blank" href="https://github.com/codespaces/new/SharmilaShroff/image-processing.py?resume=1">Open in codespace</a>




    
      
  <h1 class="sr-only">SharmilaShroff/image-processing.py</h1>
  <div class="clearfix container-xl px-md-4 px-lg-5 px-3">
    <div>

  <div style="max-width: 100%" data-view-component="true" class="Layout Layout--flowRow-until-md react-repos-overview-margin Layout--sidebarPosition-end Layout--sidebarPosition-flowRow-end">
  <div data-view-component="true" class="Layout-main">      <link crossorigin="anonymous" media="all" rel="stylesheet" href="./blue_filter_files/primer-react.47239ec6cbe68138fe4c.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./blue_filter_files/8.b14b6fddffe5b4a1fb97.module.css">

<react-partial partial-name="repos-overview" data-ssr="true" data-attempted-ssr="true" data-react-profiling="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"initialPayload":{"allShortcutsEnabled":true,"path":"/","repo":{"id":1098386497,"defaultBranch":"main","name":"image-processing.py","ownerLogin":"SharmilaShroff","currentUserCanPush":true,"isFork":false,"isEmpty":false,"createdAt":"2025-11-17T21:42:25.000+05:30","ownerAvatar":"https://avatars.githubusercontent.com/u/190357636?v=4","public":true,"private":false,"isOrgOwned":false},"currentUser":{"id":190357636,"login":"SharmilaShroff","userEmail":"sharmilashroff512@gmail.com"},"refInfo":{"name":"main","listCacheKey":"v0:1763395945.0","canEdit":true,"refType":"branch","currentOid":"dea4000e90744fd0dea754f6bce0c0316ea771cb"},"tree":{"items":[{"name":"README.md","path":"README.md","contentType":"file"},{"name":"blur_filter.py","path":"blur_filter.py","contentType":"file"},{"name":"display_img.py","path":"display_img.py","contentType":"file"},{"name":"display_img_using_link.py","path":"display_img_using_link.py","contentType":"file"},{"name":"flower.jpg","path":"flower.jpg","contentType":"file"},{"name":"live_gesture_detection.py","path":"live_gesture_detection.py","contentType":"file"},{"name":"tinted_output.py","path":"tinted_output.py","contentType":"file"},{"name":"upload_and_display_img.py","path":"upload_and_display_img.py","contentType":"file"},{"name":"upload_pdf.py","path":"upload_pdf.py","contentType":"file"}],"templateDirectorySuggestionUrl":null,"readme":null,"totalCount":9,"showBranchInfobar":false},"fileTree":null,"fileTreeProcessingTime":null,"foldersToFetch":[],"userNameDisplayConfiguration":null,"treeExpanded":false,"symbolsExpanded":false,"copilotSWEAgentEnabled":false,"isOverview":true,"overview":{"banners":{"shouldRecommendReadme":true,"isPersonalRepo":false,"showUseActionBanner":false,"actionSlug":null,"actionId":null,"showProtectBranchBanner":false,"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_repo","releasePath":"/SharmilaShroff/image-processing.py/releases/new?marketplace=true","showPublishActionBanner":false},"interactionLimitBanner":null,"showInvitationBanner":false,"inviterName":null,"actionsMigrationBannerInfo":{"releaseTags":[],"showImmutableActionsMigrationBanner":false,"initialMigrationStatus":null},"showDeployBanner":false,"detectedStack":{"framework":null,"packageManager":null}},"codeButton":{"contactPath":"/contact","isEnterprise":false,"local":{"protocolInfo":{"httpAvailable":true,"sshAvailable":true,"httpUrl":"https://github.com/SharmilaShroff/image-processing.py.git","showCloneWarning":true,"sshUrl":"git@github.com:SharmilaShroff/image-processing.py.git","sshCertificatesRequired":false,"sshCertificatesAvailable":null,"ghCliUrl":"gh repo clone SharmilaShroff/image-processing.py","defaultProtocol":"http","newSshKeyUrl":"/settings/ssh/new","setProtocolPath":"/users/set_protocol"},"platformInfo":{"cloneUrl":"https://desktop.github.com","showVisualStudioCloneButton":false,"visualStudioCloneUrl":"https://windows.github.com","showXcodeCloneButton":false,"xcodeCloneUrl":"xcode://clone?repo=https%3A%2F%2Fgithub.com%2FSharmilaShroff%2Fimage-processing.py","zipballUrl":"/SharmilaShroff/image-processing.py/archive/refs/heads/main.zip"}},"repoPolicyInfo":{"allowed":true,"canBill":true,"changesWouldBeSafe":true,"disabledByBusiness":false,"disabledByOrganization":false,"hasIpAllowLists":false},"currentUserIsEnterpriseManaged":false,"enterpriseManagedBusinessName":null,"codespacesEnabled":true,"hasAccessToCodespaces":true},"popovers":{"rename":null,"renamedParentRepo":null},"commitCount":"10","overviewFiles":[{"displayName":"README.md","repoName":"image-processing.py","refName":"main","path":"README.md","preferredFileType":"readme","tabName":"README","richText":"\u003carticle class=\"markdown-body entry-content container-lg\" itemprop=\"text\"\u003e\u003cdiv class=\"markdown-heading\" dir=\"auto\"\u003e\u003ch1 tabindex=\"-1\" class=\"heading-element\" dir=\"auto\"\u003eblur_img.py\u003c/h1\u003e\u003ca id=\"user-content-blur_imgpy\" class=\"anchor\" aria-label=\"Permalink: blur_img.py\" href=\"#blur_imgpy\"\u003e\u003csvg class=\"octicon octicon-link\" viewBox=\"0 0 16 16\" version=\"1.1\" width=\"16\" height=\"16\" aria-hidden=\"true\"\u003e\u003cpath d=\"m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z\"\u003e\u003c/path\u003e\u003c/svg\u003e\u003c/a\u003e\u003c/div\u003e\n\u003cp dir=\"auto\"\u003eA Python script that loads an image, applies a strong box blur using Pillow (PIL), and displays the blurred output with Matplotlib.\u003c/p\u003e\n\u003c/article\u003e","loaded":true,"timedOut":false,"errorMessage":null,"headerInfo":{"toc":[{"level":1,"text":"blur_img.py","anchor":"blur_imgpy","htmlText":"blur_img.py"}],"siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2FSharmilaShroff%2Fimage-processing.py"}}],"overviewFilesProcessingTime":0,"copilotSWEAgentEnabled":false,"createFromTemplatePath":"/new?template_name=image-processing.py\u0026template_owner=SharmilaShroff"}},"appPayload":{"helpUrl":"https://docs.github.com","findFileWorkerPath":"/assets-cdn/worker/find-file-worker-0cea8c6113ab.js","findInFileWorkerPath":"/assets-cdn/worker/find-in-file-worker-dc3831241a86.js","githubDevUrl":"https://github.dev/","enabled_features":{"copilot_workspace":false,"code_nav_ui_events":false,"react_blob_overlay":true,"accessible_code_button":true}}}}</script>
  <div data-target="react-partial.reactRoot"> <!-- --> <!-- --> <div class="OverviewContent-module__Box--AAyU2"><div class="OverviewHeader-module__Box--XXfuL"></div><div class="OverviewContent-module__Box_1--BhUvC"><div class="OverviewContent-module__Box_2--VG_ln"><div class="OverviewContent-module__Box_3--x_JdB"><button type="button" aria-haspopup="true" aria-expanded="false" tabindex="0" style="min-width:0" aria-label="main branch" data-testid="anchor-button" class="prc-Button-ButtonBase-9n-Xk overview-ref-selector width-full RefSelectorAnchoredOverlay-module__RefSelectorOverlayBtn--D34zl" data-loading="false" data-size="medium" data-variant="default" id="ref-picker-repos-header-ref-selector" data-hotkey="w"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="text" class="prc-Button-Label-FWkx3"><div class="RefSelectorAnchoredOverlay-module__RefSelectorOverlayContainer--mCbv8"><div class="RefSelectorAnchoredOverlay-module__RefSelectorOverlayHeader--D4cnZ"><svg aria-hidden="true" focusable="false" class="octicon octicon-git-branch" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path></svg></div><div class="ref-selector-button-text-container RefSelectorAnchoredOverlay-module__RefSelectorBtnTextContainer--yO402"><span class="RefSelectorAnchoredOverlay-module__RefSelectorText--bxVhQ">&nbsp;<!-- -->main</span></div></div></span><span data-component="trailingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></span></button><button hidden="" data-testid="ref-selector-hotkey-button" data-hotkey-scope="read-only-cursor-text-area" data-hotkey="w"></button></div><div class="OverviewContent-module__Box_4--GdyrA"><a type="button" href="https://github.com/SharmilaShroff/image-processing.py/branches" class="prc-Button-ButtonBase-9n-Xk OverviewContent-module__Button--bbZn8" data-loading="false" data-size="medium" data-variant="invisible"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-git-branch" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path></svg></span><span data-component="text" class="prc-Button-Label-FWkx3"><span><strong class="color-fg-default">1 </strong>Branch</span></span></span></a><a type="button" href="https://github.com/SharmilaShroff/image-processing.py/tags" class="prc-Button-ButtonBase-9n-Xk OverviewContent-module__Button--bbZn8" data-loading="false" data-size="medium" data-variant="invisible"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-tag" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1 7.775V2.75C1 1.784 1.784 1 2.75 1h5.025c.464 0 .91.184 1.238.513l6.25 6.25a1.75 1.75 0 0 1 0 2.474l-5.026 5.026a1.75 1.75 0 0 1-2.474 0l-6.25-6.25A1.752 1.752 0 0 1 1 7.775Zm1.5 0c0 .066.026.13.073.177l6.25 6.25a.25.25 0 0 0 .354 0l5.025-5.025a.25.25 0 0 0 0-.354l-6.25-6.25a.25.25 0 0 0-.177-.073H2.75a.25.25 0 0 0-.25.25ZM6 5a1 1 0 1 1 0 2 1 1 0 0 1 0-2Z"></path></svg></span><span data-component="text" class="prc-Button-Label-FWkx3"><span><strong class="color-fg-default">0 </strong>Tags</span></span></span></a></div><div class="OverviewContent-module__Box_5--wttWN"><a type="button" aria-label="Go to Branches page" href="https://github.com/SharmilaShroff/image-processing.py/branches" class="prc-Button-ButtonBase-9n-Xk OverviewContent-module__Button_1--AQow7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible"><svg aria-hidden="true" focusable="false" class="octicon octicon-git-branch" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path></svg></a><a type="button" aria-label="Go to Tags page" href="https://github.com/SharmilaShroff/image-processing.py/tags" class="prc-Button-ButtonBase-9n-Xk OverviewContent-module__Button_1--AQow7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="invisible"><svg aria-hidden="true" focusable="false" class="octicon octicon-tag" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1 7.775V2.75C1 1.784 1.784 1 2.75 1h5.025c.464 0 .91.184 1.238.513l6.25 6.25a1.75 1.75 0 0 1 0 2.474l-5.026 5.026a1.75 1.75 0 0 1-2.474 0l-6.25-6.25A1.752 1.752 0 0 1 1 7.775Zm1.5 0c0 .066.026.13.073.177l6.25 6.25a.25.25 0 0 0 .354 0l5.025-5.025a.25.25 0 0 0 0-.354l-6.25-6.25a.25.25 0 0 0-.177-.073H2.75a.25.25 0 0 0-.25.25ZM6 5a1 1 0 1 1 0 2 1 1 0 0 1 0-2Z"></path></svg></a></div></div><div class="OverviewContent-module__Box_6--tJpBe"><div class="OverviewContent-module__Box_7--x594V"><button hidden="" data-hotkey="t,Shift+T"></button><div class="OverviewContent-module__Box_8--TjDBQ"><div class="Box-sc-62in7e-0 OverviewContent-module__FileResultsList--ZnbCo"><span class="TextInput__StyledTextInput-sc-ttxlvl-0 d-flex FileResultsList-module__FilesSearchBox--fSAh3 TextInput-wrapper prc-components-TextInputWrapper-Hpdqi prc-components-TextInputBaseWrapper-wY-n0" data-leading-visual="true" data-trailing-visual="true" aria-busy="false"><span class="TextInput-icon" id=":rl:" aria-hidden="true"><svg aria-hidden="true" focusable="false" class="octicon octicon-search" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path></svg></span><input type="text" aria-label="Go to file" role="combobox" aria-controls="file-results-list" aria-expanded="false" aria-haspopup="dialog" autocorrect="off" spellcheck="false" placeholder="Go to file" aria-describedby=":rl: :rm:" data-component="input" class="prc-components-Input-IwWrt" value=""><span class="TextInput-icon" id=":rm:" aria-hidden="true"><kbd>t</kbd></span></span></div></div><div class="OverviewContent-module__Box_9--kxlwV"><button type="button" class="prc-Button-ButtonBase-9n-Xk" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="text" class="prc-Button-Label-FWkx3">Go to file</span></span></button></div><div><h2 class="sr-only ScreenReaderHeading-module__userSelectNone--vlUbc prc-Heading-Heading-MtWFE" data-testid="screen-reader-heading">Add file</h2><button type="button" aria-label="Add file" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-9n-Xk" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" id=":Ra35ab:"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="text" class="prc-Button-Label-FWkx3"><span class="react-directory-add-file-button">Add file<svg aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span><svg aria-hidden="true" focusable="false" class="octicon octicon-plus react-directory-add-file-icon" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path></svg></span></span></button></div></div><button type="button" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-9n-Xk" data-loading="false" data-size="medium" data-variant="primary" id=":R75ab:"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-code hide-sm" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path></svg></span><span data-component="text" class="prc-Button-Label-FWkx3">Code</span><span data-component="trailingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg></span></span></button><div class="OverviewContent-module__Box_10--UMc9C"><button data-component="IconButton" type="button" aria-haspopup="true" aria-expanded="false" tabindex="0" class="prc-Button-ButtonBase-9n-Xk prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="medium" data-variant="default" aria-labelledby=":R7p5ab:" id=":R95ab:"><svg aria-hidden="true" focusable="false" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="n" aria-hidden="true" id=":R7p5ab:" popover="auto">Open more actions menu</span></div></div></div><div class="OverviewContent-module__Box_11--QeUk1"><div data-hpc="true"><button hidden="" data-testid="focus-next-element-button" data-hotkey="j"></button><button hidden="" data-testid="focus-previous-element-button" data-hotkey="k"></button><h2 class="sr-only ScreenReaderHeading-module__userSelectNone--vlUbc prc-Heading-Heading-MtWFE" data-testid="screen-reader-heading" id="folders-and-files">Folders and files</h2><table class="Table-module__Box--KyMHK" aria-labelledby="folders-and-files"><thead class="DirectoryContent-module__OverviewHeaderRow--FlrUZ Table-module__Box_1--DkRqs"><tr class="Table-module__Box_2--l1wjV"><th colspan="2" class="DirectoryContent-module__Box--y3Nvf"><span class="text-bold">Name</span></th><th colspan="1" class="DirectoryContent-module__Box_1--xeAhp"><span class="text-bold">Name</span></th><th class="hide-sm"><div class="width-fit prc-Truncate-Truncate-2G1eo" data-inline="true" title="Last commit message" style="--truncate-max-width:125px"><span class="text-bold">Last commit message</span></div></th><th colspan="1" class="DirectoryContent-module__Box_2--h912w"><div class="width-fit prc-Truncate-Truncate-2G1eo" data-inline="true" title="Last commit date" style="--truncate-max-width:125px"><span class="text-bold">Last commit date</span></div></th></tr></thead><tbody><tr class="DirectoryContent-module__Box_3--zI0N1"><td colspan="3" class="bgColor-muted p-1 rounded-top-2"><div class="LatestCommit-module__Box--Fimpo"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone--vlUbc prc-Heading-Heading-MtWFE" data-testid="screen-reader-heading">Latest commit</h2><div data-testid="latest-commit" class="LatestCommit-module__Box_1--aQ5OG"><div class="CommitAttribution-module__CommitAttributionContainer--Si80C"><div data-testid="author-avatar" class="Box-sc-62in7e-0 AuthorAvatar-module__AuthorAvatarContainer--Z1TF8"><a class="Link__StyledLink-sc-1syctfj-0 prc-Link-Link-9ZwDx" href="https://github.com/SharmilaShroff" data-testid="avatar-icon-link" data-hovercard-url="/users/SharmilaShroff/hovercard" aria-keyshortcuts="Alt+ArrowUp"><img data-component="Avatar" class="Box-sc-62in7e-0 kglDHV AuthorAvatar-module__authorAvatarImage--bQzij prc-Avatar-Avatar-0xaUi" alt="SharmilaShroff" width="20" height="20" src="./blue_filter_files/190357636(2)" data-testid="github-avatar" aria-label="SharmilaShroff" style="--avatarSize-regular: 20px;"></a><a class="Link__StyledLink-sc-1syctfj-0 iIGVMW AuthorAvatar-module__authorHoverableLink--vw9qe prc-Link-Link-9ZwDx" data-muted="true" href="https://github.com/SharmilaShroff/image-processing.py/commits?author=SharmilaShroff" aria-label="commits by SharmilaShroff" data-hovercard-url="/users/SharmilaShroff/hovercard" aria-keyshortcuts="Alt+ArrowUp">SharmilaShroff</a></div><span class=""></span></div><div class="d-none d-sm-flex LatestCommit-module__Box_2--JDY37"><div class="Truncate flex-items-center f5"><span class="Text__StyledText-sc-1klmep6-0 Truncate-text prc-Text-Text-9mHv3" data-testid="latest-commit-html"><a href="https://github.com/SharmilaShroff/image-processing.py/commit/dea4000e90744fd0dea754f6bce0c0316ea771cb" class="Link--secondary" data-pjax="true" data-hovercard-url="/SharmilaShroff/image-processing.py/commit/dea4000e90744fd0dea754f6bce0c0316ea771cb/hovercard" aria-keyshortcuts="Alt+ArrowUp">Add image display using Streamlit</a></span></div></div><span class="d-flex d-sm-none fgColor-muted f6"><relative-time tense="past" datetime="2025-12-26T14:50:47.000Z" title="Dec 26, 2025, 8:20 PM GMT+5:30"><template shadowrootmode="open">last week</template>Dec 26, 2025</relative-time></span></div><div class="d-flex flex-shrink-0 gap-2"><div data-testid="latest-commit-details" class="d-none d-sm-flex flex-items-center"><span class="d-flex flex-nowrap fgColor-muted f6"><a class="Link--secondary prc-Link-Link-9ZwDx" aria-label="Commit dea4000" data-hovercard-url="/SharmilaShroff/image-processing.py/commit/dea4000e90744fd0dea754f6bce0c0316ea771cb/hovercard" href="https://github.com/SharmilaShroff/image-processing.py/commit/dea4000e90744fd0dea754f6bce0c0316ea771cb" data-discover="true" aria-keyshortcuts="Alt+ArrowUp">dea4000</a>&nbsp;·&nbsp;<relative-time tense="past" datetime="2025-12-26T14:50:47.000Z" title="Dec 26, 2025, 8:20 PM GMT+5:30"><template shadowrootmode="open">last week</template>Dec 26, 2025</relative-time></span></div><div class="d-flex gap-2"><h2 class="sr-only ScreenReaderHeading-module__userSelectNone--vlUbc prc-Heading-Heading-MtWFE" data-testid="screen-reader-heading">History</h2><a href="https://github.com/SharmilaShroff/image-processing.py/commits/main/" class="prc-Button-ButtonBase-9n-Xk d-none d-lg-flex LinkButton-module__code-view-link-button--thtqc flex-items-center fgColor-default" data-loading="false" data-size="small" data-variant="invisible"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-history" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path></svg></span><span data-component="text" class="prc-Button-Label-FWkx3"><span class="fgColor-default">10 Commits</span></span></span></a><div class="d-sm-none"><button data-component="IconButton" type="button" aria-pressed="false" aria-expanded="false" data-testid="latest-commit-details-toggle" class="prc-Button-ButtonBase-9n-Xk LatestCommit-module__IconButton--Zxaob prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="small" data-variant="invisible" aria-labelledby=":r10:"><svg aria-hidden="true" focusable="false" class="octicon octicon-ellipsis" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M0 5.75C0 4.784.784 4 1.75 4h12.5c.966 0 1.75.784 1.75 1.75v4.5A1.75 1.75 0 0 1 14.25 12H1.75A1.75 1.75 0 0 1 0 10.25ZM12 7a1 1 0 1 0 0 2 1 1 0 0 0 0-2ZM7 8a1 1 0 1 0 2 0 1 1 0 0 0-2 0ZM4 7a1 1 0 1 0 0 2 1 1 0 0 0 0-2Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" aria-hidden="true" id=":r10:" popover="auto">Open commit details</span></div><div class="d-flex d-lg-none"><span role="tooltip" aria-label="10 Commits" id="history-icon-button-tooltip" class="prc-Tooltip-Tooltip-JLsri prc-Tooltip-Tooltip--n-SqCQ- tooltipped-n"><a aria-label="View commit history for this file." href="https://github.com/SharmilaShroff/image-processing.py/commits/main/" class="prc-Button-ButtonBase-9n-Xk LinkButton-module__code-view-link-button--thtqc flex-items-center fgColor-default" data-loading="false" data-size="small" data-variant="invisible" aria-describedby="history-icon-button-tooltip"><span data-component="buttonContent" data-align="center" class="prc-Button-ButtonContent-Iohp5"><span data-component="leadingVisual" class="prc-Button-Visual-YNt2F prc-Button-VisualWrap-E4cnq"><svg aria-hidden="true" focusable="false" class="octicon octicon-history" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path></svg></span></span></a></span></div></div></div></div></td></tr><tr class="react-directory-row undefined" id="folder-row-0"><td class="react-directory-row-name-cell-small-screen" colspan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="README.md" aria-label="README.md, (File)" class="Link--primary" href="https://github.com/SharmilaShroff/image-processing.py/blob/main/README.md" data-discover="true">README.md</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colspan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="README.md" aria-label="README.md, (File)" class="Link--primary" href="https://github.com/SharmilaShroff/image-processing.py/blob/main/README.md" data-discover="true">README.md</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div><div class="react-directory-commit-message"><a data-pjax="true" title="Initial commit" class="Link--secondary" href="https://github.com/SharmilaShroff/image-processing.py/commit/e6b14f532660f4ed5d9ffa6de42b0d97beb26f4a">Initial commit</a></div></div></td><td><div class="react-directory-commit-age"><relative-time tense="past" datetime="2025-11-17T16:12:25.000Z" title="Nov 17, 2025, 9:42 PM GMT+5:30"><template shadowrootmode="open">2 months ago</template>Nov 17, 2025</relative-time></div></td></tr><tr class="react-directory-row undefined" id="folder-row-1"><td class="react-directory-row-name-cell-small-screen" colspan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="blur_filter.py" aria-label="blur_filter.py, (File)" class="Link--primary" href="https://github.com/SharmilaShroff/image-processing.py/blob/main/blur_filter.py" data-discover="true">blur_filter.py</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colspan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="blur_filter.py" aria-label="blur_filter.py, (File)" class="Link--primary" href="https://github.com/SharmilaShroff/image-processing.py/blob/main/blur_filter.py" data-discover="true">blur_filter.py</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div><div class="react-directory-commit-message"><a data-pjax="true" title="Add blur filter to image processing script" class="Link--secondary" href="https://github.com/SharmilaShroff/image-processing.py/commit/abe9b99fd9bedbbbebab55b4ee26aa53cd5ca69c">Add blur filter to image processing script</a></div></div></td><td><div class="react-directory-commit-age"><relative-time tense="past" datetime="2025-11-17T16:15:20.000Z" title="Nov 17, 2025, 9:45 PM GMT+5:30"><template shadowrootmode="open">2 months ago</template>Nov 17, 2025</relative-time></div></td></tr><tr class="react-directory-row undefined" id="folder-row-2"><td class="react-directory-row-name-cell-small-screen" colspan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="display_img.py" aria-label="display_img.py, (File)" class="Link--primary" href="https://github.com/SharmilaShroff/image-processing.py/blob/main/display_img.py" data-discover="true">display_img.py</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colspan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="display_img.py" aria-label="display_img.py, (File)" class="Link--primary" href="https://github.com/SharmilaShroff/image-processing.py/blob/main/display_img.py" data-discover="true">display_img.py</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div><div class="react-directory-commit-message"><a data-pjax="true" title="Add installation comment for dependencies

Added a comment for installing required packages." class="Link--secondary" href="https://github.com/SharmilaShroff/image-processing.py/commit/d4c2e3238fc9b1cbac061dc475c5efefb0dc449b">Add installation comment for dependencies</a></div></div></td><td><div class="react-directory-commit-age"><relative-time tense="past" datetime="2025-12-26T14:16:59.000Z" title="Dec 26, 2025, 7:46 PM GMT+5:30"><template shadowrootmode="open">last week</template>Dec 26, 2025</relative-time></div></td></tr><tr class="react-directory-row undefined" id="folder-row-3"><td class="react-directory-row-name-cell-small-screen" colspan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="display_img_using_link.py" aria-label="display_img_using_link.py, (File)" class="Link--primary" href="https://github.com/SharmilaShroff/image-processing.py/blob/main/display_img_using_link.py" data-discover="true">display_img_using_link.py</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colspan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="display_img_using_link.py" aria-label="display_img_using_link.py, (File)" class="Link--primary" href="https://github.com/SharmilaShroff/image-processing.py/blob/main/display_img_using_link.py" data-discover="true">display_img_using_link.py</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div><div class="react-directory-commit-message"><a data-pjax="true" title="Add image display using Streamlit" class="Link--secondary" href="https://github.com/SharmilaShroff/image-processing.py/commit/dea4000e90744fd0dea754f6bce0c0316ea771cb">Add image display using Streamlit</a></div></div></td><td><div class="react-directory-commit-age"><relative-time tense="past" datetime="2025-12-26T14:50:47.000Z" title="Dec 26, 2025, 8:20 PM GMT+5:30"><template shadowrootmode="open">last week</template>Dec 26, 2025</relative-time></div></td></tr><tr class="react-directory-row undefined" id="folder-row-4"><td class="react-directory-row-name-cell-small-screen" colspan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="flower.jpg" aria-label="flower.jpg, (File)" class="Link--primary" href="https://github.com/SharmilaShroff/image-processing.py/blob/main/flower.jpg" data-discover="true">flower.jpg</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colspan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="flower.jpg" aria-label="flower.jpg, (File)" class="Link--primary" href="https://github.com/SharmilaShroff/image-processing.py/blob/main/flower.jpg" data-discover="true">flower.jpg</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div><div class="react-directory-commit-message"><a data-pjax="true" title="Add files via upload" class="Link--secondary" href="https://github.com/SharmilaShroff/image-processing.py/commit/d78038d6b0a70cc2684fa74a0a356c296b6eed6e">Add files via upload</a></div></div></td><td><div class="react-directory-commit-age"><relative-time tense="past" datetime="2025-11-18T16:54:35.000Z" title="Nov 18, 2025, 10:24 PM GMT+5:30"><template shadowrootmode="open">2 months ago</template>Nov 18, 2025</relative-time></div></td></tr><tr class="react-directory-row undefined" id="folder-row-5"><td class="react-directory-row-name-cell-small-screen" colspan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="live_gesture_detection.py" aria-label="live_gesture_detection.py, (File)" class="Link--primary" href="https://github.com/SharmilaShroff/image-processing.py/blob/main/live_gesture_detection.py" data-discover="true">live_gesture_detection.py</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colspan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="live_gesture_detection.py" aria-label="live_gesture_detection.py, (File)" class="Link--primary" href="https://github.com/SharmilaShroff/image-processing.py/blob/main/live_gesture_detection.py" data-discover="true">live_gesture_detection.py</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div><div class="react-directory-commit-message"><a data-pjax="true" title="Implement live gesture detection with speech output

This script captures video from the webcam and recognizes hand gestures using MediaPipe, converting them into speech output." class="Link--secondary" href="https://github.com/SharmilaShroff/image-processing.py/commit/ee2f8fe0ef310dbafd18ba0880a202d6647fe7b1">Implement live gesture detection with speech output</a></div></div></td><td><div class="react-directory-commit-age"><relative-time tense="past" datetime="2025-12-26T14:10:14.000Z" title="Dec 26, 2025, 7:40 PM GMT+5:30"><template shadowrootmode="open">last week</template>Dec 26, 2025</relative-time></div></td></tr><tr class="react-directory-row undefined" id="folder-row-6"><td class="react-directory-row-name-cell-small-screen" colspan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="tinted_output.py" aria-label="tinted_output.py, (File)" class="Link--primary" href="https://github.com/SharmilaShroff/image-processing.py/blob/main/tinted_output.py" data-discover="true">tinted_output.py</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colspan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="tinted_output.py" aria-label="tinted_output.py, (File)" class="Link--primary" href="https://github.com/SharmilaShroff/image-processing.py/blob/main/tinted_output.py" data-discover="true">tinted_output.py</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div><div class="react-directory-commit-message"><a data-pjax="true" title="Add blue tint effect to image display" class="Link--secondary" href="https://github.com/SharmilaShroff/image-processing.py/commit/061ff9d0b75ef77617f9e0624066bbb50f771a8d">Add blue tint effect to image display</a></div></div></td><td><div class="react-directory-commit-age"><relative-time tense="past" datetime="2025-11-18T16:51:42.000Z" title="Nov 18, 2025, 10:21 PM GMT+5:30"><template shadowrootmode="open">2 months ago</template>Nov 18, 2025</relative-time></div></td></tr><tr class="react-directory-row undefined" id="folder-row-7"><td class="react-directory-row-name-cell-small-screen" colspan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="upload_and_display_img.py" aria-label="upload_and_display_img.py, (File)" class="Link--primary" href="https://github.com/SharmilaShroff/image-processing.py/blob/main/upload_and_display_img.py" data-discover="true">upload_and_display_img.py</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colspan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="upload_and_display_img.py" aria-label="upload_and_display_img.py, (File)" class="Link--primary" href="https://github.com/SharmilaShroff/image-processing.py/blob/main/upload_and_display_img.py" data-discover="true">upload_and_display_img.py</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div><div class="react-directory-commit-message"><a data-pjax="true" title="Add image upload and display functionality" class="Link--secondary" href="https://github.com/SharmilaShroff/image-processing.py/commit/1ac45fdb99a49eacb86d50e3058903138fc1190b">Add image upload and display functionality</a></div></div></td><td><div class="react-directory-commit-age"><relative-time tense="past" datetime="2025-12-26T14:25:38.000Z" title="Dec 26, 2025, 7:55 PM GMT+5:30"><template shadowrootmode="open">last week</template>Dec 26, 2025</relative-time></div></td></tr><tr class="react-directory-row undefined" id="folder-row-8"><td class="react-directory-row-name-cell-small-screen" colspan="2"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="upload_pdf.py" aria-label="upload_pdf.py, (File)" class="Link--primary" href="https://github.com/SharmilaShroff/image-processing.py/blob/main/upload_pdf.py" data-discover="true">upload_pdf.py</a></div></div></div></div></td><td class="react-directory-row-name-cell-large-screen" colspan="1"><div class="react-directory-filename-column"><svg aria-hidden="true" focusable="false" class="octicon octicon-file color-fg-muted" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></svg><div class="overflow-hidden"><div class="react-directory-filename-cell"><div class="react-directory-truncate"><a title="upload_pdf.py" aria-label="upload_pdf.py, (File)" class="Link--primary" href="https://github.com/SharmilaShroff/image-processing.py/blob/main/upload_pdf.py" data-discover="true">upload_pdf.py</a></div></div></div></div></td><td class="react-directory-row-commit-cell"><div><div class="react-directory-commit-message"><a data-pjax="true" title="Add PDF upload functionality with Streamlit" class="Link--secondary" href="https://github.com/SharmilaShroff/image-processing.py/commit/09dde25e2fa4006b5ea91aaaf2badd405865fa87">Add PDF upload functionality with Streamlit</a></div></div></td><td><div class="react-directory-commit-age"><relative-time tense="past" datetime="2025-12-26T14:44:57.000Z" title="Dec 26, 2025, 8:14 PM GMT+5:30"><template shadowrootmode="open">last week</template>Dec 26, 2025</relative-time></div></td></tr><tr class="d-none DirectoryContent-module__Box_4--QyUbd" data-testid="view-all-files-row"><td colspan="3" class="DirectoryContent-module__Box_5--OJZQU"><div><button class="prc-Link-Link-9ZwDx">View all files</button></div></td></tr></tbody></table><document-dropzone data-catalyst=""><div class="repo-file-upload-tree-target js-upload-manifest-tree-view" data-testid="dragzone" data-drop-url="/SharmilaShroff/image-processing.py/upload/main" data-target="document-dropzone.dropContainer"><div class="repo-file-upload-outline"><div class="repo-file-upload-slate"><div class="fgColor-muted"><svg aria-hidden="true" focusable="false" class="octicon octicon-file" viewBox="0 0 24 24" width="32" height="32" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M3 3a2 2 0 0 1 2-2h9.982a2 2 0 0 1 1.414.586l4.018 4.018A2 2 0 0 1 21 7.018V21a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2Zm2-.5a.5.5 0 0 0-.5.5v18a.5.5 0 0 0 .5.5h14a.5.5 0 0 0 .5-.5V8.5h-4a2 2 0 0 1-2-2v-4Zm10 0v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 0-.146-.336l-4.018-4.018A.5.5 0 0 0 15 2.5Z"></path></svg></div><h2 aria-hidden="true">Drop to upload your files</h2></div></div></div></document-dropzone></div><div class="OverviewRepoFiles-module__Box_1--yBtNT"><div class="OverviewRepoFiles-module__Box_2--w5aD8"><div itemscope="" itemtype="https://schema.org/abstract" class="OverviewRepoFiles-module__Box_3--ELDBz"><h2 class="prc-src-InternalVisuallyHidden-2YaI6">Repository files navigation</h2><nav class="prc-components-UnderlineWrapper-eT-Yj OverviewRepoFiles-module__UnderlineNav--uKbU6" aria-label="Repository files" data-variant="inset"><ul class="prc-components-UnderlineItemList-xKlKC" role="list"><li class="prc-UnderlineNav-UnderlineNavItem-syRjR"><a href="https://github.com/SharmilaShroff/image-processing.py#" aria-current="page" class="prc-components-UnderlineItem-7fP-n"><span data-component="icon"><svg aria-hidden="true" focusable="false" class="octicon octicon-book" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M0 1.75A.75.75 0 0 1 .75 1h4.253c1.227 0 2.317.59 3 1.501A3.743 3.743 0 0 1 11.006 1h4.245a.75.75 0 0 1 .75.75v10.5a.75.75 0 0 1-.75.75h-4.507a2.25 2.25 0 0 0-1.591.659l-.622.621a.75.75 0 0 1-1.06 0l-.622-.621A2.25 2.25 0 0 0 5.258 13H.75a.75.75 0 0 1-.75-.75Zm7.251 10.324.004-5.073-.002-2.253A2.25 2.25 0 0 0 5.003 2.5H1.5v9h3.757a3.75 3.75 0 0 1 1.994.574ZM8.755 4.75l-.004 7.322a3.752 3.752 0 0 1 1.992-.572H14.5v-9h-3.495a2.25 2.25 0 0 0-2.25 2.25Z"></path></svg></span><span data-component="text" data-content="README">README</span></a></li></ul></nav><button data-component="IconButton" type="button" title="Edit file" class="prc-Button-ButtonBase-9n-Xk IconButton__StyledIconButton-sc-i53dt6-0 jCdPVA prc-Button-IconButton-fyge7" data-loading="false" data-no-visuals="true" data-size="small" data-variant="invisible" aria-labelledby=":Rj9ab:" data-hotkey="e,Shift+E"><svg aria-hidden="true" focusable="false" class="octicon octicon-pencil" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M11.013 1.427a1.75 1.75 0 0 1 2.474 0l1.086 1.086a1.75 1.75 0 0 1 0 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 0 1-.927-.928l.929-3.25c.081-.286.235-.547.445-.758l8.61-8.61Zm.176 4.823L9.75 4.81l-6.286 6.287a.253.253 0 0 0-.064.108l-.558 1.953 1.953-.558a.253.253 0 0 0 .108-.064Zm1.238-3.763a.25.25 0 0 0-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 0 0 0-.354Z"></path></svg></button><span class="prc-TooltipV2-Tooltip-tLeuB" data-direction="s" aria-hidden="true" id=":Rj9ab:" popover="auto">Edit file</span></div><div class="Box-sc-62in7e-0 js-snippet-clipboard-copy-unpositioned DirectoryRichtextContent-module__SharedMarkdownContent--BTKsc" data-hpc="true"><article class="markdown-body entry-content container-lg" itemprop="text"><div class="markdown-heading" dir="auto"><h1 tabindex="-1" class="heading-element" dir="auto">blur_img.py</h1><a id="user-content-blur_imgpy" class="anchor" aria-label="Permalink: blur_img.py" href="https://github.com/SharmilaShroff/image-processing.py#blur_imgpy"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto">A Python script that loads an image, applies a strong box blur using Pillow (PIL), and displays the blurred output with Matplotlib.</p>
</article></div></div></div></div></div> <!-- --> <!-- --> <script type="application/json" id="__PRIMER_DATA_:R0:__">{"resolvedServerColorMode":"day"}</script></div>
</react-partial>


      <input type="hidden" value="ZooUjCx3ZRvTYWcaZHHGMkZw8N2lYxqYeG6ZZoqofNXYQPRepzuAGRrJgtlc6DXskMRYpHULq7Z0bg4LuRM11g" data-csrf="true" id="react-codespace-csrf">
</div>
  <div data-view-component="true" class="Layout-sidebar">      

      <div class="BorderGrid about-margin" data-pjax="">
        <div class="BorderGrid-row">
          <div class="BorderGrid-cell">
              <details class="details-reset details-overlay details-overlay-dark ">
          <summary class="float-right" role="button">
        <div class="Link--secondary pt-1 pl-2">
          <svg aria-label="Edit repository metadata" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-gear float-right">
    <path d="M8 0a8.2 8.2 0 0 1 .701.031C9.444.095 9.99.645 10.16 1.29l.288 1.107c.018.066.079.158.212.224.231.114.454.243.668.386.123.082.233.09.299.071l1.103-.303c.644-.176 1.392.021 1.82.63.27.385.506.792.704 1.218.315.675.111 1.422-.364 1.891l-.814.806c-.049.048-.098.147-.088.294.016.257.016.515 0 .772-.01.147.038.246.088.294l.814.806c.475.469.679 1.216.364 1.891a7.977 7.977 0 0 1-.704 1.217c-.428.61-1.176.807-1.82.63l-1.102-.302c-.067-.019-.177-.011-.3.071a5.909 5.909 0 0 1-.668.386c-.133.066-.194.158-.211.224l-.29 1.106c-.168.646-.715 1.196-1.458 1.26a8.006 8.006 0 0 1-1.402 0c-.743-.064-1.289-.614-1.458-1.26l-.289-1.106c-.018-.066-.079-.158-.212-.224a5.738 5.738 0 0 1-.668-.386c-.123-.082-.233-.09-.299-.071l-1.103.303c-.644.176-1.392-.021-1.82-.63a8.12 8.12 0 0 1-.704-1.218c-.315-.675-.111-1.422.363-1.891l.815-.806c.05-.048.098-.147.088-.294a6.214 6.214 0 0 1 0-.772c.01-.147-.038-.246-.088-.294l-.815-.806C.635 6.045.431 5.298.746 4.623a7.92 7.92 0 0 1 .704-1.217c.428-.61 1.176-.807 1.82-.63l1.102.302c.067.019.177.011.3-.071.214-.143.437-.272.668-.386.133-.066.194-.158.211-.224l.29-1.106C6.009.645 6.556.095 7.299.03 7.53.01 7.764 0 8 0Zm-.571 1.525c-.036.003-.108.036-.137.146l-.289 1.105c-.147.561-.549.967-.998 1.189-.173.086-.34.183-.5.29-.417.278-.97.423-1.529.27l-1.103-.303c-.109-.03-.175.016-.195.045-.22.312-.412.644-.573.99-.014.031-.021.11.059.19l.815.806c.411.406.562.957.53 1.456a4.709 4.709 0 0 0 0 .582c.032.499-.119 1.05-.53 1.456l-.815.806c-.081.08-.073.159-.059.19.162.346.353.677.573.989.02.03.085.076.195.046l1.102-.303c.56-.153 1.113-.008 1.53.27.161.107.328.204.501.29.447.222.85.629.997 1.189l.289 1.105c.029.109.101.143.137.146a6.6 6.6 0 0 0 1.142 0c.036-.003.108-.036.137-.146l.289-1.105c.147-.561.549-.967.998-1.189.173-.086.34-.183.5-.29.417-.278.97-.423 1.529-.27l1.103.303c.109.029.175-.016.195-.045.22-.313.411-.644.573-.99.014-.031.021-.11-.059-.19l-.815-.806c-.411-.406-.562-.957-.53-1.456a4.709 4.709 0 0 0 0-.582c-.032-.499.119-1.05.53-1.456l.815-.806c.081-.08.073-.159.059-.19a6.464 6.464 0 0 0-.573-.989c-.02-.03-.085-.076-.195-.046l-1.102.303c-.56.153-1.113.008-1.53-.27a4.44 4.44 0 0 0-.501-.29c-.447-.222-.85-.629-.997-1.189l-.289-1.105c-.029-.11-.101-.143-.137-.146a6.6 6.6 0 0 0-1.142 0ZM11 8a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM9.5 8a1.5 1.5 0 1 0-3.001.001A1.5 1.5 0 0 0 9.5 8Z"></path>
</svg>
        </div>
      </summary>

  <details-dialog class="Box d-flex flex-column anim-fade-in fast Box-overlay--wide overflow-x-hidden" aria-label="Edit repository details" role="dialog" aria-modal="true">
    <div class="Box-header">
      <button class="Box-btn-octicon btn-octicon float-right" type="button" aria-label="Close dialog" data-close-dialog="">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
      </button>
        <h1 class="Box-title">Edit repository details</h1>
    </div>
      <div class="Box-body overflow-auto">
              <div class="js-topic-form-area">
        <!-- '"` --><!-- </textarea></xmp> --><form id="repo_metadata_form" data-turbo="false" action="https://github.com/SharmilaShroff/image-processing.py/settings/update_meta" accept-charset="UTF-8" method="post"><input type="hidden" name="_method" value="put" autocomplete="off"><input type="hidden" name="authenticity_token" value="AzqWeaTIBmrjrfIvkZdcDjdDkPM9jhpSU1y2GdrqhLWAk7fTkvRZ8hzm7DEaFI9ypnvQ9GrGNVT6Za_h_RLFBg">
          <div class="form-group mt-0 mb-3 js-length-limited-input-container">
            <div class="mb-2">
              <label for="repo_description">Description</label>
            </div>
            <input type="text" id="repo_description" class="form-control input-contrast width-full js-length-limited-input" name="repo_description" placeholder="Short description of this repository" autofocus="" value="A Python script that loads an image, applies a strong box blur using Pillow (PIL), and displays the blurred output with Matplotlib." data-input-max-length="350" data-warning-length="50" data-warning-text="{{remaining}} characters remaining">
            <div class="d-none mt-1 js-length-limited-input-warning text-right color-fg-danger"></div>
          </div>
          <div class="form-group my-3">
            <div class="mb-2">
              <label for="repo_homepage">Website</label>
            </div>
             <input type="url" id="repo_homepage" class="color-bg-default form-control input-contrast width-full" name="repo_homepage" value="" placeholder="Enter a valid URL">
          </div>
          <div class="width-full tag-input-container topic-input-container d-inline-block js-tag-input-container">
            <div class="js-tag-input-wrapper">
              <div class="form-group my-0">
                <div class="mb-2">
                  <label for="repo_topics" class="d-block">Topics <span class="text-normal color-fg-muted">(separate with spaces)</span></label>
                </div>
                <div class="tag-input form-control d-inline-block color-bg-default py-0 position-relative">
                  <ul class="js-tag-input-selected-tags d-inline">
                    <li class="d-none topic-tag-action my-1 mr-1 f6 float-left js-tag-input-tag js-template">
                      <span class="js-placeholder-tag-name"></span>
                      <button type="button" class="delete-topic-button f5 no-underline ml-1 js-remove" tabindex="-1">
                        <svg aria-label="Remove topic" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
                      </button>
                      <input type="hidden" name="repo_topics[]" class="js-topic-input" value="">
                    </li>

                  </ul>

                    <auto-complete src="/SharmilaShroff/image-processing.py/topic_autocomplete" for="repo-topic-popup">
                      <input type="text" id="repo_topics" class="tag-input-inner form-control color-bg-default short d-inline-block p-0 my-1 border-0" autocomplete="off" autofocus="" role="combobox" aria-controls="repo-topic-popup" aria-expanded="false" aria-autocomplete="list" aria-haspopup="listbox" spellcheck="false">
                      <ul class="suggester border width-full color-bg-default left-0" id="repo-topic-popup" style="top: 100%;" hidden="" aria-label="results" role="listbox"></ul>
                    </auto-complete>
                </div>
              </div>
            </div>
          </div>

          <div class="form-group mt-3 mb-0" role="group" aria-labelledby="hidden_sidebar_options">
            <div class="text-bold mb-2" id="hidden_sidebar_options">Include in the home page</div>
            <label class="d-block mb-2 text-normal">
              <input name="repo_sections[releases]" type="hidden" value="0" autocomplete="off"><input class="mr-1" type="checkbox" value="1" checked="checked" name="repo_sections[releases]" id="repo_sections_releases"> Releases
            </label>
            <label class="d-block mb-2 text-normal">
              <input name="repo_sections[packages]" type="hidden" value="0" autocomplete="off"><input class="mr-1" type="checkbox" value="1" checked="checked" name="repo_sections[packages]" id="repo_sections_packages"> Packages
            </label>

            <label class="d-block text-normal">
              <input name="repo_sections[deployments]" type="hidden" value="0" autocomplete="off"><input class="mr-1" type="checkbox" value="1" checked="checked" name="repo_sections[deployments]" id="repo_sections_deployments"> Deployments
            </label>
          </div>
</form>      </div>

      </div>
        <div class="Box-footer">
                <div class="form-actions">
        <button type="submit" class="btn btn-primary" form="repo_metadata_form">Save changes</button>
        <button type="reset" class="btn" data-close-dialog="" form="repo_metadata_form">Cancel</button>
      </div>

        </div>
  </details-dialog>
</details>
<div class="hide-sm hide-md">
  <h2 class="mb-3 h4">About</h2>

      <p class="f4 my-3">
        A Python script that loads an image, applies a strong box blur using Pillow (PIL), and displays the blurred output with Matplotlib.
      </p>


    <h3 class="sr-only">Resources</h3>
    <div class="mt-2">
      <a class="Link--muted" data-analytics-event="{&quot;category&quot;:&quot;Repository Overview&quot;,&quot;action&quot;:&quot;click&quot;,&quot;label&quot;:&quot;location:sidebar;file:readme&quot;}" href="https://github.com/SharmilaShroff/image-processing.py#readme-ov-file">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-book mr-2">
    <path d="M0 1.75A.75.75 0 0 1 .75 1h4.253c1.227 0 2.317.59 3 1.501A3.743 3.743 0 0 1 11.006 1h4.245a.75.75 0 0 1 .75.75v10.5a.75.75 0 0 1-.75.75h-4.507a2.25 2.25 0 0 0-1.591.659l-.622.621a.75.75 0 0 1-1.06 0l-.622-.621A2.25 2.25 0 0 0 5.258 13H.75a.75.75 0 0 1-.75-.75Zm7.251 10.324.004-5.073-.002-2.253A2.25 2.25 0 0 0 5.003 2.5H1.5v9h3.757a3.75 3.75 0 0 1 1.994.574ZM8.755 4.75l-.004 7.322a3.752 3.752 0 0 1 1.992-.572H14.5v-9h-3.495a2.25 2.25 0 0 0-2.25 2.25Z"></path>
</svg>
        Readme
</a>    </div>

  





  <include-fragment src="/SharmilaShroff/image-processing.py/hovercards/citation/sidebar_partial?tree_name=main" data-nonce="v2:2b815f31-74b1-a9f7-c69b-a73f6467a217" data-view-component="true" class="is-error"><template shadowrootmode="open"><style>:host {display: block;}</style><slot></slot></template>
  

  <div data-show-on-forbidden-error="" hidden="">
    <div class="Box">
  <div class="blankslate-container">
    <div data-view-component="true" class="blankslate blankslate-spacious color-bg-default rounded-2">
      

      <h3 data-view-component="true" class="blankslate-heading">        Uh oh!
</h3>
      <p data-view-component="true">        </p><p class="color-fg-muted my-2 mb-2 ws-normal">There was an error while loading. <a class="Link--inTextBlock" data-turbo="false" href="https://github.com/SharmilaShroff/image-processing.py" aria-label="Please reload this page">Please reload this page</a>.</p>
<p></p>

</div>  </div>
</div>  </div>
</include-fragment>
    <div class="mt-2">
      <a href="https://github.com/SharmilaShroff/image-processing.py/activity" data-view-component="true" class="Link Link--muted"><svg text="gray" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-pulse mr-2">
    <path d="M6 2c.306 0 .582.187.696.471L10 10.731l1.304-3.26A.751.751 0 0 1 12 7h3.25a.75.75 0 0 1 0 1.5h-2.742l-1.812 4.528a.751.751 0 0 1-1.392 0L6 4.77 4.696 8.03A.75.75 0 0 1 4 8.5H.75a.75.75 0 0 1 0-1.5h2.742l1.812-4.529A.751.751 0 0 1 6 2Z"></path>
</svg>
        <span class="color-fg-muted">Activity</span></a>    </div>


    <h3 class="sr-only">Stars</h3>
    <div class="mt-2">
      <a href="https://github.com/SharmilaShroff/image-processing.py/stargazers" data-view-component="true" class="Link Link--muted"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star mr-2">
    <path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Zm0 2.445L6.615 5.5a.75.75 0 0 1-.564.41l-3.097.45 2.24 2.184a.75.75 0 0 1 .216.664l-.528 3.084 2.769-1.456a.75.75 0 0 1 .698 0l2.77 1.456-.53-3.084a.75.75 0 0 1 .216-.664l2.24-2.183-3.096-.45a.75.75 0 0 1-.564-.41L8 2.694Z"></path>
</svg>
        <strong>0</strong>
        stars</a>    </div>

    <h3 class="sr-only">Watchers</h3>
    <div class="mt-2">
      <a href="https://github.com/SharmilaShroff/image-processing.py/watchers" data-view-component="true" class="Link Link--muted"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-eye mr-2">
    <path d="M8 2c1.981 0 3.671.992 4.933 2.078 1.27 1.091 2.187 2.345 2.637 3.023a1.62 1.62 0 0 1 0 1.798c-.45.678-1.367 1.932-2.637 3.023C11.67 13.008 9.981 14 8 14c-1.981 0-3.671-.992-4.933-2.078C1.797 10.83.88 9.576.43 8.898a1.62 1.62 0 0 1 0-1.798c.45-.677 1.367-1.931 2.637-3.022C4.33 2.992 6.019 2 8 2ZM1.679 7.932a.12.12 0 0 0 0 .136c.411.622 1.241 1.75 2.366 2.717C5.176 11.758 6.527 12.5 8 12.5c1.473 0 2.825-.742 3.955-1.715 1.124-.967 1.954-2.096 2.366-2.717a.12.12 0 0 0 0-.136c-.412-.621-1.242-1.75-2.366-2.717C10.824 4.242 9.473 3.5 8 3.5c-1.473 0-2.825.742-3.955 1.715-1.124.967-1.954 2.096-2.366 2.717ZM8 10a2 2 0 1 1-.001-3.999A2 2 0 0 1 8 10Z"></path>
</svg>
        <strong>0</strong>
        watching</a>    </div>

    <h3 class="sr-only">Forks</h3>
    <div class="mt-2">
      <a href="https://github.com/SharmilaShroff/image-processing.py/forks" data-view-component="true" class="Link Link--muted"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo-forked mr-2">
    <path d="M5 5.372v.878c0 .414.336.75.75.75h4.5a.75.75 0 0 0 .75-.75v-.878a2.25 2.25 0 1 1 1.5 0v.878a2.25 2.25 0 0 1-2.25 2.25h-1.5v2.128a2.251 2.251 0 1 1-1.5 0V8.5h-1.5A2.25 2.25 0 0 1 3.5 6.25v-.878a2.25 2.25 0 1 1 1.5 0ZM5 3.25a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Zm6.75.75a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5Zm-3 8.75a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Z"></path>
</svg>
        <strong>0</strong>
        forks</a>    </div>


</div>

          </div>
        </div>

        
            <div class="BorderGrid-row">
              <div class="BorderGrid-cell">
                <h2 class="h4 mb-3" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame">
  <a href="https://github.com/SharmilaShroff/image-processing.py/releases" data-view-component="true" class="Link--primary no-underline Link" data-turbo-frame="repo-content-turbo-frame">Releases</a></h2>

    <div class="text-small color-fg-muted">No releases published</div>
    <div class=" text-small"><a class="Link--inTextBlock" href="https://github.com/SharmilaShroff/image-processing.py/releases/new">Create a new release</a></div>

              </div>
            </div>

        
        
            <div class="BorderGrid-row">
              <div class="BorderGrid-cell">
                
  <h2 class="h4 mb-3">
  <a href="https://github.com/users/SharmilaShroff/packages?repo_name=image-processing.py" data-view-component="true" class="Link--primary no-underline Link d-flex flex-items-center">Packages
      <span title="0" hidden="hidden" data-view-component="true" class="Counter ml-1">0</span></a></h2>


      <div class="text-small color-fg-muted">
        No packages published <br>
          <a class="Link--inTextBlock" href="https://github.com/SharmilaShroff/image-processing.py/packages">Publish your first package</a>
      </div>



              </div>
            </div>

        
        
        
        
            <div class="BorderGrid-row">
              <div class="BorderGrid-cell">
                <h2 class="h4 mb-3">Languages</h2>
<div class="mb-2">
  <span data-view-component="true" class="Progress">
    <span style="background-color:#3572A5 !important;;width: 100.0%;" itemprop="keywords" data-view-component="true" class="Progress-item color-bg-success-emphasis"></span>
</span></div>
<ul class="list-style-none">
    <li class="d-inline">
        <a class="d-inline-flex flex-items-center flex-nowrap Link--secondary no-underline text-small mr-3" href="https://github.com/SharmilaShroff/image-processing.py/search?l=python" data-ga-click="Repository, language stats search click, location:repo overview">
          <svg style="color:#3572A5;" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-dot-fill mr-2">
    <path d="M8 4a4 4 0 1 1 0 8 4 4 0 0 1 0-8Z"></path>
</svg>
          <span class="color-fg-default text-bold mr-1">Python</span>
          <span>100.0%</span>
        </a>
    </li>
</ul>

              </div>
            </div>

        
              <div class="BorderGrid-row js-notice">
  <div class="BorderGrid-cell">
    <div data-view-component="true" class="Subhead border-bottom-0 mb-2">
  <h2 data-view-component="true" class="h4 Subhead-heading Subhead-heading--large">        Suggested workflows
</h2>
  <div data-view-component="true" class="Subhead-description">         Based on your tech stack
</div>
  
</div>    <ol class="list-style-none">
        <li class="list-style-none">
          <div data-view-component="true" class="mb-2 p-3 border rounded-2">
  <div data-view-component="true" class="d-flex flex-items-stretch">
    <div aria-hidden="true" style="color: #00ADD8 !important; background-color: var(--bgColor-white, var(--color-scale-white)) !important; width: 32px !important; height: 32px !important; min-width: 32px !important;" data-view-component="true" class="CircleBadge">
      <img class="CircleBadge-icon" src="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyBmaWxsPSJub25lIiB2ZXJzaW9uPSIxLjEiIHZpZXdCb3g9IjAgMCAxNDAgMTQwIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMzEpIiBjbGlwLXBhdGg9InVybCgjYSkiPgo8cGF0aCBkPSJtMTYxLjUzIDMuMDk5NGUtNSAwLjM4NS0wLjQzNTQzLTcuNDkzLTYuNjIyMi0zLjMxMSAzLjc0NjVjLTAuOTg5IDEuMTE4NC0xLjk5MSAyLjIyMjItMy4wMDggMy4zMTExaC0xMTcuMXY3Ljc5MTlsLTYuODc5OSA0LjI0MDMgMi42MjM0IDQuMjU2NWMxLjM3MzUgMi4yMjg1IDIuNzkyOSA0LjQxOTYgNC4yNTY1IDYuNTcyNHY5My40MjFjLTAuMDMzOSAxZS0zIC0wLjA2NzggMWUtMyAtMC4xMDE4IDJlLTNsLTQuOTk4OSAwLjEwMiAwLjIwMzUgOS45OTggNC44OTcyLTAuMXYxMy43MTZoMTQwdi04OC42ODRjMS40NC0yLjA3MzQgMi44NC00LjE4MyA0LjE5Ni02LjMyODIgMi4yNzktMy40MjkyIDMuOTcxLTYuMzYxMyA1LjEwMy04LjQ1NzkgMC41Ny0xLjA1NCAwLjk5OC0xLjg5ODYgMS4yOS0yLjQ5MTIgMC4xNDYtMC4yOTY0IDAuMjU4LTAuNTI5OSAwLjMzNi0wLjY5NTMgMC4wMzktMC4wODI3IDAuMDY5LTAuMTQ4NCAwLjA5MS0wLjE5NjRsMC4wMjctMC4wNTg3IDllLTMgLTAuMDE5MiAzZS0zIC0wLjAwNzEgMWUtMyAtMC4wMDI5IDFlLTMgLTAuMDAxM2MwLTZlLTQgMC0wLjAwMTEtNC41NTctMi4wNTc4bDQuNTU3IDIuMDU2NyAyLjA1Ny00LjU1NzUtOS4xMTUtNC4xMTMyLTIuMDU0IDQuNTUxOHYxZS0zbC0xZS0zIDllLTQgLTFlLTMgMC4wMDE3djJlLTNsLThlLTMgMC4wMTc0Yy0wLjAxMSAwLjAyMzQtMC4wMyAwLjA2NDItMC4wNTcgMC4xMjE2LTAuMDU0IDAuMTE1LTAuMTQxIDAuMjk2Ny0wLjI2MSAwLjUzOTktMC4yMzkgMC40ODY2LTAuNjExIDEuMjE4OC0xLjExNiAyLjE1NS0wLjE1NSAwLjI4NTktMC4zMjIgMC41OTA3LTAuNTAxIDAuOTEzMXYtMzIuNjl6bTAgMGgtMTMuNDI3Yy0yMi4wNDYgMjMuNjE4LTUwLjU5MSA0MC4yNDYtODEuOTkxIDQ3Ljc3OS0xMS44NzUtMTAuNTQxLTIyLjMwNS0yMi44NzEtMzAuODUxLTM2LjczN2wtMi42MjM0LTQuMjU2NS0xLjYzMzEgMS4wMDY1djE1LjA2OWM4LjcwNzYgMTIuODA3IDE4Ljk4MiAyNC4yNTkgMzAuNDgyIDM0LjE1NiAxNi41MyAxNC4yMjYgMzUuNTkxIDI1LjI0MiA1Ni4xNyAzMi40NjEtMTcuNDI0IDExLjM4Ny0zNi45NjIgMTkuNDQ4LTU3LjYxMiAyMy42MDUtOS40Nzc0IDEuOTA3LTE5LjE5IDIuOTkyLTI5LjA0IDMuMTk5djEwLjAwMmwwLjEwMTgtMmUtM2MxMC40ODQtMC4yMTMgMjAuODIzLTEuMzY1IDMwLjkxMS0zLjM5NiAyNS40MDMtNS4xMTMgNDkuMjE3LTE1Ljc5NiA2OS43ODYtMzEuMDkgMTUuMDEtMTEuMTYxIDI4LjI5Mi0yNC43NzkgMzkuMjAxLTQwLjQ4di0xOC42MjZjLTAuOTk2IDEuNzkwOC0yLjM4IDQuMTI3LTQuMTYzIDYuODA4bC0wLjAzMyAwLjA0OTEtMC4wMzEgMC4wNDk4Yy0xMC41MTIgMTYuNjM5LTIzLjc1OSAzMS4wMTUtMzguOTYyIDQyLjY4LTE4Ljg4MS01LjcwOS0zNi41NTUtMTQuNzU4LTUyLjE4LTI2LjY2MiAzMS45ODItOS4xMjkyIDYwLjgyNy0yNy4yNSA4Mi45NjktNTIuMzA0eiIgY2xpcC1ydWxlPSJldmVub2RkIiBmaWxsPSIjZjAzMTAwIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiLz4KPC9nPgo8ZGVmcz4KPGNsaXBQYXRoIGlkPSJhIj4KPHBhdGggZD0ibTMxIDI4YzAtMTUuNDY0IDEyLjUzNi0yOCAyOC0yOGg4NGMxNS40NjQgMCAyOCAxMi41MzYgMjggMjh2ODRjMCAxNS40NjQtMTIuNTM2IDI4LTI4IDI4aC04NGMtMTUuNDY0IDAtMjgtMTIuNTM2LTI4LTI4eiIgZmlsbD0iI2ZmZiIvPgo8L2NsaXBQYXRoPgo8L2RlZnM+Cjwvc3ZnPgo=" alt="SLSA Generic generator logo">
</div>
    <div data-view-component="true" class="d-flex flex-column">
      <span data-view-component="true" class="f5 text-bold ml-2">SLSA Generic generator</span>
      <span data-view-component="true" class="color-fg-muted ml-2 text-small"></span>
</div>    <a href="https://github.com/SharmilaShroff/image-processing.py/new/main?filename=.github%2Fworkflows%2Fgenerator-generic-ossf-slsa3-publish.yml&amp;workflow_template=ci%2Fgenerator-generic-ossf-slsa3-publish" data-hydro-click="{&quot;event_type&quot;:&quot;actions.onboarding_setup_workflow_click&quot;,&quot;payload&quot;:{&quot;repository_id&quot;:1098386497,&quot;workflow_template&quot;:&quot;ci/generator-generic-ossf-slsa3-publish&quot;,&quot;view_section&quot;:&quot;repository_sidebar&quot;,&quot;view_rank&quot;:1,&quot;templates_count&quot;:3,&quot;template_creator&quot;:&quot;Open Source Security Foundation (OpenSSF)&quot;,&quot;new_with_filter_view&quot;:false,&quot;correlation_id&quot;:&quot;CE1F:99196:279A32:2B14D1:695BCE6F&quot;,&quot;category&quot;:&quot;Continuous integration&quot;,&quot;search_query&quot;:null,&quot;template_source_visibility&quot;:&quot;shared&quot;,&quot;originating_url&quot;:&quot;https://github.com/SharmilaShroff/image-processing.py&quot;,&quot;user_id&quot;:190357636}}" data-hydro-click-hmac="3d46d26bdbdc5a9f0ae0ed569d0f6dc503c7e2694ba42394feb004deae67db70" style="min-width: 80px" aria-describedby="slsa-generic-generator-description" data-view-component="true" class="Button--secondary Button--small Button ml-auto">  <span class="Button-content">
    <span class="Button-label">Configure<span class="sr-only">&nbsp;SLSA Generic generator</span></span>
  </span>
</a>
</div>  <span id="slsa-generic-generator-description" aria-hidden="true" data-view-component="true" class="d-flex color-fg-muted f6 ml-5 mt-1 pl-2">Generate SLSA3 provenance for your existing release workflows</span>
</div>
        </li>
        <li class="list-style-none">
          <div data-view-component="true" class="mb-2 p-3 border rounded-2">
  <div data-view-component="true" class="d-flex flex-items-stretch">
    <div aria-hidden="true" style="color: #3572A5 !important; background-color: var(--bgColor-white, var(--color-scale-white)) !important; width: 32px !important; height: 32px !important; min-width: 32px !important;" data-view-component="true" class="CircleBadge">
      <img class="CircleBadge-icon" src="data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBoZWlnaHQ9IjQ4IiB3aWR0aD0iNDgiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTTAgMjMuNTkxYy4wMi0uMDY2LjAzNi0uMTM0LjA0NS0uMjAyLjAzNy0uNjk3LjA0NS0xLjQwMi4xMi0yLjEuMTE3LTIuMjYuODcxLTQuNDQgMi4xNzUtNi4yOWE2LjMyMiA2LjMyMiAwIDAxNS4wODUtMi41NjVIMjMuNjFjLjMxNSAwIC4zMTUgMCAuMzE1LS4zMTV2LTEuMTI1YzAtLjIzMi0uMDY4LS4yODQtLjI4NS0uMjg0SDEyLjYyM2MtLjE4OCAwLS4yNTUtLjA1My0uMjU1LS4yNDhWNC45NjZjLjAzNi0uNzk2LjM2OC0xLjU1LjkzLTIuMTE1YTYuNjgzIDYuNjgzIDAgMDEyLjcwNy0xLjc0NyAxNi42NjggMTYuNjY4IDAgMDEzLjktLjg5MiAzMi44NDMgMzIuODQzIDAgMDE1LjQ4Mi0uMTY1YzEuOTcyLjAzNyAzLjkyMy4zOTkgNS43NzYgMS4wNzJhNy4wOTUgNy4wOTUgMCAwMTMuMjQgMi4yNSA0LjUzNiA0LjUzNiAwIDAxLjk0NSAzLjA3NGMtLjA0NS45MyAwIDEuODY3IDAgMi44MDR2NS4xOWMwIDEuMDE5IDAgMi4wNDYtLjA0NSAzLjA1OGE1LjQyMSA1LjQyMSAwIDAxLTMuNTE4IDUuMDQgOC4wNDIgOC4wNDIgMCAwMS0zLjE0My41OTloLTExLjQ2YTYuNTQgNi41NCAwIDAwLTMuNDUuOTA3IDUuOTk5IDUuOTk5IDAgMDAtMi42NDcgMy43MDQgOC42NTYgOC42NTYgMCAwMC0uMzIzIDIuMzc3djUuMTk2YzAgLjM0NSAwIC4zMzgtLjM0NS4zNDUtMS4yNDUgMC0yLjQ5LjAzOC0zLjc1IDBBNS4yNSA1LjI1IDAgMDEzLjM0NSAzNC4zYTguMjQ4IDguMjQ4IDAgMDEtMi4yOTUtMy41NTQgMTUuMTQyIDE1LjE0MiAwIDAxLS44NDgtMy44NDdjLS4wNzUtLjg0LS4xMDUtMS42OC0uMTU3LTIuNTEyQTIuNDc1IDIuNDc1IDAgMDAwIDI0LjExdi0uNTE4eiIgZmlsbD0iIzM3NzJhNCIvPjxwYXRoIGQ9Ik0xNS4yMDMgNS43MzhhMi4xMDcgMi4xMDcgMCAxMDIuMTA3LTIuMTIyIDIuMTIzIDIuMTIzIDAgMDAtMi4xMDcgMi4xMjJ6IiBmaWxsPSIjMDAwIi8+PHBhdGggZD0iTTE1LjIwMyA1LjczOGEyLjExIDIuMTEgMCAxMTQuMjIgMCAyLjExIDIuMTEgMCAwMS00LjIyIDB6IiBmaWxsPSIjZmZmIi8+PHBhdGggZD0iTTQ4IDI0LjQwMWMtLjAyLjA2Ni0uMDM2LjEzNC0uMDQ1LjIwMy0uMDM3LjY5Ny0uMDQ1IDEuNDAyLS4xMiAyLjFhMTEuOTk1IDExLjk5NSAwIDAxLTIuMTc1IDYuMjkgNi4zMjIgNi4zMjIgMCAwMS01LjA4NSAyLjU3MkgyNC4zOWMtLjMxNSAwLS4zMTUgMC0uMzE1LjMxNXYxLjEyNWMwIC4yMzIuMDY4LjI4NS4yODUuMjg1aDExLjAxOGMuMTg3IDAgLjI1NS4wNTIuMjU1LjI0N3Y1LjQ5NmEzLjIwOSAzLjIwOSAwIDAxLS45MyAyLjExNSA2LjY4MyA2LjY4MyAwIDAxLTIuNzA4IDEuNzQ3IDE2LjY2OSAxNi42NjkgMCAwMS0zLjg5Mi44OTJjLTEuODIuMjA4LTMuNjU0LjI2My01LjQ4My4xNjVhMTcuODc3IDE3Ljg3NyAwIDAxLTUuNzc1LTEuMDcyIDcuMDk1IDcuMDk1IDAgMDEtMy4yNC0yLjI1IDQuNTM2IDQuNTM2IDAgMDEtLjk0NS0zLjA3NGMuMDQ1LS45MyAwLTEuODY3IDAtMi44MDR2LTUuMTljMC0xLjAxOSAwLTIuMDQ2LjA0NS0zLjA1OGE1LjQyIDUuNDIgMCAwMTMuNTE3LTUuMDQgOC4wNDIgOC4wNDIgMCAwMTMuMTQzLS41OTloMTEuNDUzYTYuNTQgNi41NCAwIDAwMy40NS0uOTA3IDYgNiAwIDAwMi42NDctMy43MTIgOC42NiA4LjY2IDAgMDAuMzIzLTIuMzc3di01LjE5NmMwLS4zNDUgMC0uMzM3LjM0NS0uMzQ1IDEuMjQ1IDAgMi40OS0uMDM3IDMuNzUgMGE1LjI1IDUuMjUgMCAwMTMuMzIyIDEuMzY1IDguMjQ5IDguMjQ5IDAgMDEyLjI5NSAzLjU1NCAxNS4xNSAxNS4xNSAwIDAxLjg0IDMuODYxYy4wNzUuODQuMTA1IDEuNjguMTU4IDIuNTEyLjAxLjA5MS4wMjUuMTgxLjA0NS4yNy4wMDUuMTY1LjAwNy4zMzUuMDA3LjUxeiIgZmlsbD0iI2ZmZGE0YiIvPjxwYXRoIGQ9Ik0zMi43OTcgNDEuOTkyYTIuMTA3IDIuMTA3IDAgMTAtMi4xMDcgMi4xMjIgMi4xMjMgMi4xMjMgMCAwMDIuMTA3LTIuMTIyeiIgZmlsbD0iIzAwMCIvPjxwYXRoIGQ9Ik0zMi43OTcgNDEuOTkyYTIuMTEgMi4xMSAwIDExLTQuMjIgMCAyLjExIDIuMTEgMCAwMTQuMjIgMHoiIGZpbGw9IiNmZmYiLz48L3N2Zz4=" alt="Pylint logo">
</div>
    <div data-view-component="true" class="d-flex flex-column">
      <span data-view-component="true" class="f5 text-bold ml-2">Pylint</span>
      <span data-view-component="true" class="color-fg-muted ml-2 text-small"></span>
</div>    <a href="https://github.com/SharmilaShroff/image-processing.py/new/main?filename=.github%2Fworkflows%2Fpylint.yml&amp;workflow_template=ci%2Fpylint" data-hydro-click="{&quot;event_type&quot;:&quot;actions.onboarding_setup_workflow_click&quot;,&quot;payload&quot;:{&quot;repository_id&quot;:1098386497,&quot;workflow_template&quot;:&quot;ci/pylint&quot;,&quot;view_section&quot;:&quot;repository_sidebar&quot;,&quot;view_rank&quot;:2,&quot;templates_count&quot;:3,&quot;template_creator&quot;:null,&quot;new_with_filter_view&quot;:false,&quot;correlation_id&quot;:&quot;CE1F:99196:279A32:2B14D1:695BCE6F&quot;,&quot;category&quot;:&quot;Continuous integration&quot;,&quot;search_query&quot;:null,&quot;template_source_visibility&quot;:&quot;shared&quot;,&quot;originating_url&quot;:&quot;https://github.com/SharmilaShroff/image-processing.py&quot;,&quot;user_id&quot;:190357636}}" data-hydro-click-hmac="17b813584e223c686608989f9b85285dacf68cf6fb1aced2479cad4d485d0c3d" style="min-width: 80px" aria-describedby="pylint-description" data-view-component="true" class="Button--secondary Button--small Button ml-auto">  <span class="Button-content">
    <span class="Button-label">Configure<span class="sr-only">&nbsp;Pylint</span></span>
  </span>
</a>
</div>  <span id="pylint-description" aria-hidden="true" data-view-component="true" class="d-flex color-fg-muted f6 ml-5 mt-1 pl-2">Lint a Python application with pylint.</span>
</div>
        </li>
        <li class="list-style-none">
          <div data-view-component="true" class="mb-2 p-3 border rounded-2">
  <div data-view-component="true" class="d-flex flex-items-stretch">
    <div aria-hidden="true" style="color: #3572A5 !important; background-color: var(--bgColor-white, var(--color-scale-white)) !important; width: 32px !important; height: 32px !important; min-width: 32px !important;" data-view-component="true" class="CircleBadge">
      <img class="CircleBadge-icon" src="data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBoZWlnaHQ9IjQ4IiB3aWR0aD0iNDgiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTTAgMjMuNTkxYy4wMi0uMDY2LjAzNi0uMTM0LjA0NS0uMjAyLjAzNy0uNjk3LjA0NS0xLjQwMi4xMi0yLjEuMTE3LTIuMjYuODcxLTQuNDQgMi4xNzUtNi4yOWE2LjMyMiA2LjMyMiAwIDAxNS4wODUtMi41NjVIMjMuNjFjLjMxNSAwIC4zMTUgMCAuMzE1LS4zMTV2LTEuMTI1YzAtLjIzMi0uMDY4LS4yODQtLjI4NS0uMjg0SDEyLjYyM2MtLjE4OCAwLS4yNTUtLjA1My0uMjU1LS4yNDhWNC45NjZjLjAzNi0uNzk2LjM2OC0xLjU1LjkzLTIuMTE1YTYuNjgzIDYuNjgzIDAgMDEyLjcwNy0xLjc0NyAxNi42NjggMTYuNjY4IDAgMDEzLjktLjg5MiAzMi44NDMgMzIuODQzIDAgMDE1LjQ4Mi0uMTY1YzEuOTcyLjAzNyAzLjkyMy4zOTkgNS43NzYgMS4wNzJhNy4wOTUgNy4wOTUgMCAwMTMuMjQgMi4yNSA0LjUzNiA0LjUzNiAwIDAxLjk0NSAzLjA3NGMtLjA0NS45MyAwIDEuODY3IDAgMi44MDR2NS4xOWMwIDEuMDE5IDAgMi4wNDYtLjA0NSAzLjA1OGE1LjQyMSA1LjQyMSAwIDAxLTMuNTE4IDUuMDQgOC4wNDIgOC4wNDIgMCAwMS0zLjE0My41OTloLTExLjQ2YTYuNTQgNi41NCAwIDAwLTMuNDUuOTA3IDUuOTk5IDUuOTk5IDAgMDAtMi42NDcgMy43MDQgOC42NTYgOC42NTYgMCAwMC0uMzIzIDIuMzc3djUuMTk2YzAgLjM0NSAwIC4zMzgtLjM0NS4zNDUtMS4yNDUgMC0yLjQ5LjAzOC0zLjc1IDBBNS4yNSA1LjI1IDAgMDEzLjM0NSAzNC4zYTguMjQ4IDguMjQ4IDAgMDEtMi4yOTUtMy41NTQgMTUuMTQyIDE1LjE0MiAwIDAxLS44NDgtMy44NDdjLS4wNzUtLjg0LS4xMDUtMS42OC0uMTU3LTIuNTEyQTIuNDc1IDIuNDc1IDAgMDAwIDI0LjExdi0uNTE4eiIgZmlsbD0iIzM3NzJhNCIvPjxwYXRoIGQ9Ik0xNS4yMDMgNS43MzhhMi4xMDcgMi4xMDcgMCAxMDIuMTA3LTIuMTIyIDIuMTIzIDIuMTIzIDAgMDAtMi4xMDcgMi4xMjJ6IiBmaWxsPSIjMDAwIi8+PHBhdGggZD0iTTE1LjIwMyA1LjczOGEyLjExIDIuMTEgMCAxMTQuMjIgMCAyLjExIDIuMTEgMCAwMS00LjIyIDB6IiBmaWxsPSIjZmZmIi8+PHBhdGggZD0iTTQ4IDI0LjQwMWMtLjAyLjA2Ni0uMDM2LjEzNC0uMDQ1LjIwMy0uMDM3LjY5Ny0uMDQ1IDEuNDAyLS4xMiAyLjFhMTEuOTk1IDExLjk5NSAwIDAxLTIuMTc1IDYuMjkgNi4zMjIgNi4zMjIgMCAwMS01LjA4NSAyLjU3MkgyNC4zOWMtLjMxNSAwLS4zMTUgMC0uMzE1LjMxNXYxLjEyNWMwIC4yMzIuMDY4LjI4NS4yODUuMjg1aDExLjAxOGMuMTg3IDAgLjI1NS4wNTIuMjU1LjI0N3Y1LjQ5NmEzLjIwOSAzLjIwOSAwIDAxLS45MyAyLjExNSA2LjY4MyA2LjY4MyAwIDAxLTIuNzA4IDEuNzQ3IDE2LjY2OSAxNi42NjkgMCAwMS0zLjg5Mi44OTJjLTEuODIuMjA4LTMuNjU0LjI2My01LjQ4My4xNjVhMTcuODc3IDE3Ljg3NyAwIDAxLTUuNzc1LTEuMDcyIDcuMDk1IDcuMDk1IDAgMDEtMy4yNC0yLjI1IDQuNTM2IDQuNTM2IDAgMDEtLjk0NS0zLjA3NGMuMDQ1LS45MyAwLTEuODY3IDAtMi44MDR2LTUuMTljMC0xLjAxOSAwLTIuMDQ2LjA0NS0zLjA1OGE1LjQyIDUuNDIgMCAwMTMuNTE3LTUuMDQgOC4wNDIgOC4wNDIgMCAwMTMuMTQzLS41OTloMTEuNDUzYTYuNTQgNi41NCAwIDAwMy40NS0uOTA3IDYgNiAwIDAwMi42NDctMy43MTIgOC42NiA4LjY2IDAgMDAuMzIzLTIuMzc3di01LjE5NmMwLS4zNDUgMC0uMzM3LjM0NS0uMzQ1IDEuMjQ1IDAgMi40OS0uMDM3IDMuNzUgMGE1LjI1IDUuMjUgMCAwMTMuMzIyIDEuMzY1IDguMjQ5IDguMjQ5IDAgMDEyLjI5NSAzLjU1NCAxNS4xNSAxNS4xNSAwIDAxLjg0IDMuODYxYy4wNzUuODQuMTA1IDEuNjguMTU4IDIuNTEyLjAxLjA5MS4wMjUuMTgxLjA0NS4yNy4wMDUuMTY1LjAwNy4zMzUuMDA3LjUxeiIgZmlsbD0iI2ZmZGE0YiIvPjxwYXRoIGQ9Ik0zMi43OTcgNDEuOTkyYTIuMTA3IDIuMTA3IDAgMTAtMi4xMDcgMi4xMjIgMi4xMjMgMi4xMjMgMCAwMDIuMTA3LTIuMTIyeiIgZmlsbD0iIzAwMCIvPjxwYXRoIGQ9Ik0zMi43OTcgNDEuOTkyYTIuMTEgMi4xMSAwIDExLTQuMjIgMCAyLjExIDIuMTEgMCAwMTQuMjIgMHoiIGZpbGw9IiNmZmYiLz48L3N2Zz4=" alt="Python Package using Anaconda logo">
</div>
    <div data-view-component="true" class="d-flex flex-column">
      <span data-view-component="true" class="f5 text-bold ml-2">Python Package using Anaconda</span>
      <span data-view-component="true" class="color-fg-muted ml-2 text-small"></span>
</div>    <a href="https://github.com/SharmilaShroff/image-processing.py/new/main?filename=.github%2Fworkflows%2Fpython-package-conda.yml&amp;workflow_template=ci%2Fpython-package-conda" data-hydro-click="{&quot;event_type&quot;:&quot;actions.onboarding_setup_workflow_click&quot;,&quot;payload&quot;:{&quot;repository_id&quot;:1098386497,&quot;workflow_template&quot;:&quot;ci/python-package-conda&quot;,&quot;view_section&quot;:&quot;repository_sidebar&quot;,&quot;view_rank&quot;:3,&quot;templates_count&quot;:3,&quot;template_creator&quot;:null,&quot;new_with_filter_view&quot;:false,&quot;correlation_id&quot;:&quot;CE1F:99196:279A32:2B14D1:695BCE6F&quot;,&quot;category&quot;:&quot;Continuous integration&quot;,&quot;search_query&quot;:null,&quot;template_source_visibility&quot;:&quot;shared&quot;,&quot;originating_url&quot;:&quot;https://github.com/SharmilaShroff/image-processing.py&quot;,&quot;user_id&quot;:190357636}}" data-hydro-click-hmac="bddc7cd76961b4ff96b5a663a6d23ee339e8b3ff735e8a06320c5b952916f3fe" style="min-width: 80px" aria-describedby="python-package-using-anaconda-description" data-view-component="true" class="Button--secondary Button--small Button ml-auto">  <span class="Button-content">
    <span class="Button-label">Configure<span class="sr-only">&nbsp;Python Package using Anaconda</span></span>
  </span>
</a>
</div>  <span id="python-package-using-anaconda-description" aria-hidden="true" data-view-component="true" class="d-flex color-fg-muted f6 ml-5 mt-1 pl-2">Create and test a Python package on multiple Python versions using Anaconda for package management.</span>
</div>
        </li>
    </ol>
    <div data-view-component="true" class="d-flex flex-justify-between">
      <a data-analytics-event="{&quot;category&quot;:&quot;suggested_workflows_in_repository_sidebar&quot;,&quot;action&quot;:&quot;clicked_on_see_more_button&quot;,&quot;label&quot;:&quot;owner:190357636;ref_cta:configure;ref_loc:respository_sidebar&quot;}" href="https://github.com/SharmilaShroff/image-processing.py/actions/new" data-view-component="true" class="Link">More workflows</a>
      <!-- '"` --><!-- </textarea></xmp> --><form class="js-notice-dismiss" data-turbo="false" action="https://github.com/users/SharmilaShroff/dismiss_repository_notice" accept-charset="UTF-8" method="post"><input type="hidden" name="_method" value="delete" autocomplete="off"><input type="hidden" name="authenticity_token" value="FjYAUCSDVT8jHZgZKbOBeDD9z6_bhcnOLrdxr_pjymaKQq4zH5e0nk-Y8V9KyPmlCv6UuAbUdmjnBAcw6fybTQ" autocomplete="off">
        <input type="hidden" name="notice_name" value="repo_suggested_workflows">
        <input type="hidden" name="repository_id" value="1098386497">
        <button data-analytics-event="{&quot;category&quot;:&quot;suggested_workflows_in_repository_sidebar&quot;,&quot;action&quot;:&quot;dismissed_component&quot;,&quot;label&quot;:&quot;owner:190357636;ref_cta:configure;ref_loc:respository_sidebar&quot;}" type="submit" data-view-component="true" class="Button--link Button--medium Button text-small color-fg-muted text-normal">  <span class="Button-content">
    <span class="Button-label">Dismiss suggestions</span>
  </span>
</button>

</form></div>  </div>
</div>

      </div>
</div>
  
</div></div>

  </div>


  </div>

</turbo-frame>


    </main>
  </div>

  </div>

          <footer class="footer pt-7 pb-6 f6 color-fg-muted color-border-subtle p-responsive" role="contentinfo">
  <h2 class="sr-only">Footer</h2>

  


  <div class="d-flex flex-justify-center flex-items-center flex-column-reverse flex-lg-row flex-wrap flex-lg-nowrap">
    <div class="d-flex flex-items-center flex-shrink-0 mx-2">
      <a aria-label="GitHub Homepage" class="footer-octicon mr-2" href="https://github.com/">
        <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-mark-github">
    <path d="M12 1C5.923 1 1 5.923 1 12c0 4.867 3.149 8.979 7.521 10.436.55.096.756-.233.756-.522 0-.262-.013-1.128-.013-2.049-2.764.509-3.479-.674-3.699-1.292-.124-.317-.66-1.293-1.127-1.554-.385-.207-.936-.715-.014-.729.866-.014 1.485.797 1.691 1.128.99 1.663 2.571 1.196 3.204.907.096-.715.385-1.196.701-1.471-2.448-.275-5.005-1.224-5.005-5.432 0-1.196.426-2.186 1.128-2.956-.111-.275-.496-1.402.11-2.915 0 0 .921-.288 3.024 1.128a10.193 10.193 0 0 1 2.75-.371c.936 0 1.871.123 2.75.371 2.104-1.43 3.025-1.128 3.025-1.128.605 1.513.221 2.64.111 2.915.701.77 1.127 1.747 1.127 2.956 0 4.222-2.571 5.157-5.019 5.432.399.344.743 1.004.743 2.035 0 1.471-.014 2.654-.014 3.025 0 .289.206.632.756.522C19.851 20.979 23 16.854 23 12c0-6.077-4.922-11-11-11Z"></path>
</svg>
</a>
      <span>
        © 2026 GitHub,&nbsp;Inc.
      </span>
    </div>

    <nav aria-label="Footer">
      <h3 class="sr-only" id="sr-footer-heading">Footer navigation</h3>

      <ul class="list-style-none d-flex flex-justify-center flex-wrap mb-2 mb-lg-0" aria-labelledby="sr-footer-heading">

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to Terms&quot;,&quot;label&quot;:&quot;text:terms&quot;}" href="https://docs.github.com/site-policy/github-terms/github-terms-of-service" data-view-component="true" class="Link--secondary Link">Terms</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to privacy&quot;,&quot;label&quot;:&quot;text:privacy&quot;}" href="https://docs.github.com/site-policy/privacy-policies/github-privacy-statement" data-view-component="true" class="Link--secondary Link">Privacy</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to security&quot;,&quot;label&quot;:&quot;text:security&quot;}" href="https://github.com/security" data-view-component="true" class="Link--secondary Link">Security</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to status&quot;,&quot;label&quot;:&quot;text:status&quot;}" href="https://www.githubstatus.com/" data-view-component="true" class="Link--secondary Link">Status</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to community&quot;,&quot;label&quot;:&quot;text:community&quot;}" href="https://github.community/" data-view-component="true" class="Link--secondary Link">Community</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to docs&quot;,&quot;label&quot;:&quot;text:docs&quot;}" href="https://docs.github.com/" data-view-component="true" class="Link--secondary Link">Docs</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to contact&quot;,&quot;label&quot;:&quot;text:contact&quot;}" href="https://support.github.com/?tags=dotcom-footer" data-view-component="true" class="Link--secondary Link">Contact</a>
          </li>

          <li class="mx-2">
  <cookie-consent-link data-catalyst="">
    <button type="button" class="Link--secondary underline-on-hover border-0 p-0 color-bg-transparent" data-action="click:cookie-consent-link#showConsentManagement" data-analytics-event="{&quot;location&quot;:&quot;footer&quot;,&quot;action&quot;:&quot;cookies&quot;,&quot;context&quot;:&quot;subfooter&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;cookies_link_subfooter_footer&quot;}">
       Manage cookies
    </button>
  </cookie-consent-link>
</li>

<li class="mx-2">
  <cookie-consent-link data-catalyst="">
    <button type="button" class="Link--secondary underline-on-hover border-0 p-0 color-bg-transparent text-left" data-action="click:cookie-consent-link#showConsentManagement" data-analytics-event="{&quot;location&quot;:&quot;footer&quot;,&quot;action&quot;:&quot;dont_share_info&quot;,&quot;context&quot;:&quot;subfooter&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;dont_share_info_link_subfooter_footer&quot;}">
      Do not share my personal information
    </button>
  </cookie-consent-link>
</li>

      </ul>
    </nav>
  </div>
</footer>



    <ghcc-consent id="ghcc" class="position-fixed bottom-0 left-0" style="z-index: 999999" data-locale="en" data-initial-cookie-consent-allowed="" data-cookie-consent-required="false" data-catalyst=""></ghcc-consent>




  <div id="ajax-error-message" class="ajax-error-message flash flash-error" hidden="">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
    </button>
    You can’t perform that action at this time.
  </div>

    <template id="site-details-dialog"></template>

    <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box color-shadow-large" style="width:360px;"></div>
</div>

    <template id="snippet-clipboard-copy-button"></template>
<template id="snippet-clipboard-copy-button-unpositioned"></template>


    <style>
      .user-mention[href$="/SharmilaShroff"] {
        color: var(--color-user-mention-fg);
        background-color: var(--bgColor-attention-muted, var(--color-attention-subtle));
        border-radius: 2px;
        margin-left: -2px;
        margin-right: -2px;
      }
      .user-mention[href$="/SharmilaShroff"]:before,
      .user-mention[href$="/SharmilaShroff"]:after {
        content: '';
        display: inline-block;
        width: 2px;
      }
    </style>


    </div>
    <div id="js-global-screen-reader-notice" class="sr-only mt-n1" aria-live="polite" aria-atomic="true"></div>
    <div id="js-global-screen-reader-notice-assertive" class="sr-only mt-n1" aria-live="assertive" aria-atomic="true"></div>
  


</body></html>