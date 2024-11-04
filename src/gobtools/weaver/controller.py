from gobtools.utils.client import Client

class WeaverController(Client):
    def __init__(self, path_root: str) -> None:
        super().__init__(path_root)

    def __post_releases(self, path: str, group_id: str, artifact_id: str, version: str, added_values: list[str] = None) -> dict:
        data = {
            "groupId": group_id,
            "artifactId": artifact_id,
            "version": version
        }
        if added_values:
            data["addedValues"] = added_values
        return self.post_dict(path, data)

    def get_release(self, group_id: str, artifact_id: str, version: str, added_values: list[str] = None) -> dict:
        return self.__post_releases("/release", group_id, artifact_id, version, added_values)
    
    def get_release_new_versions(self, group_id: str, artifact_id: str, version: str, added_values: list[str] = None) -> dict:
        return self.__post_releases("/release/newVersions", group_id, artifact_id, version, added_values)
    
    def get_dependents(self, group_id: str, artifact_id: str, version: str, added_values: list[str] = None) -> dict:
        return self.__post_releases("/release/dependents", group_id, artifact_id, version, added_values)

    def get_cypher(self, query: str, added_values: list[str] = None) -> dict:
        data = {
            "query": query
        }
        if added_values:
            data["addedValues"] = added_values
        return self.post_dict("/cypher", data)
    
    def __post_artifact(self, path: str, group_id: str, artifact_id: str, added_values: list[str] = None) -> dict:
        data = {
            "groupId": group_id,
            "artifactId": artifact_id
        }
        if added_values:
            data["addedValues"] = added_values
        return self.post_dict(path, data)
    
    def get_artifact(self, group_id: str, artifact_id: str, added_values: list[str] = None) -> dict:
        return self.__post_artifact(group_id, artifact_id, added_values)
    
    def get_artifact_releases(self, group_id: str, artifact_id: str, added_values: list[str] = None) -> dict:
        return self.__post_artifact("/artifact/releases", group_id, artifact_id, added_values)