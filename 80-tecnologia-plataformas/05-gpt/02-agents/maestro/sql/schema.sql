CREATE TABLE IF NOT EXISTS maestro_folder (folder_id TEXT PRIMARY KEY, path TEXT UNIQUE NOT NULL, parent_id TEXT, description TEXT, status TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS maestro_request (id TEXT PRIMARY KEY, raw_input TEXT NOT NULL, received_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE IF NOT EXISTS maestro_skill_selection (request_id TEXT NOT NULL, plugin_id TEXT NOT NULL, skill_name TEXT NOT NULL, role TEXT NOT NULL, path TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS maestro_write (request_id TEXT NOT NULL, folder_id TEXT NOT NULL, destination_path TEXT NOT NULL, classification TEXT NOT NULL, summary TEXT);
CREATE TABLE IF NOT EXISTS maestro_relation (request_id TEXT NOT NULL, source_folder_id TEXT NOT NULL, target_folder_id TEXT NOT NULL, relation_type TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS maestro_provenance (request_id TEXT NOT NULL, source_type TEXT NOT NULL, source_uri TEXT, metadata_json TEXT);
