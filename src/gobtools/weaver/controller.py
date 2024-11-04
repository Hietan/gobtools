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
