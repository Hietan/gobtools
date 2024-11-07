from gobtools.utils.client import Client


class WeaverController(Client):
    def __init__(self, path_root: str) -> None:
        super().__init__(path_root)

    def __post_with_added_values(
        self, path: str, data: dict, added_values: list[str]
    ) -> dict:
        if added_values:
            data["addedValues"] = added_values
        else:
            data["addedValues"] = []
        print(data)
        return self.post_dict(path, data)

    def __post_releases(
        self,
        path: str,
        group_id: str,
        artifact_id: str,
        version: str,
        added_values: list[str] = None,
    ) -> dict:
        data = {"groupId": group_id, "artifactId": artifact_id, "version": version}
        return self.__post_with_added_values(path, data, added_values)

    def __post_graph(
        self, releases: list[dict], added_values: list[str] = None
    ) -> dict:
        data = {"releases": releases}
        return self.__post_with_added_values("/graph", data, added_values)

    def __post_artifact(
        self, path: str, group_id: str, artifact_id: str, added_values: list[str] = None
    ) -> dict:
        data = {"groupId": group_id, "artifactId": artifact_id}
        return self.__post_with_added_values(path, data, added_values)

    def get_release(
        self,
        group_id: str,
        artifact_id: str,
        version: str,
        added_values: list[str] = None,
    ) -> dict:
        return self.__post_releases(
            "/release", group_id, artifact_id, version, added_values
        )

    def get_release_new_versions(
        self,
        group_id: str,
        artifact_id: str,
        version: str,
        added_values: list[str] = None,
    ) -> dict:
        return self.__post_releases(
            "/release/newVersions", group_id, artifact_id, version, added_values
        )

    def get_dependents(
        self,
        group_id: str,
        artifact_id: str,
        version: str,
        added_values: list[str] = None,
    ) -> dict:
        return self.__post_releases(
            "/release/dependents", group_id, artifact_id, version, added_values
        )

    def get_graph_traversing(
        self,
        start_releases_gav: list[str],
        lib_to_expands_ga: list[str],
        filters: list[str],
        added_values: list[str] = None,
    ) -> dict:
        data = {
            "startReleasesGav": start_releases_gav,
            "libToExpandsGa": lib_to_expands_ga,
            "filters": filters,
        }
        return self.__post_with_added_values("/graph/traversing", data, added_values)

    def get_graph_rooted_graph(
        self, releases: list[dict], added_values: list[str] = None
    ) -> dict:
        return self.__post_graph(releases, added_values)

    def get_graph_direct_possibilities_rooted(
        self, releases: list[dict], added_values: list[str] = None
    ) -> dict:
        return self.__post_graph(
            "/graph/directPossibilitiesRooted", releases, added_values
        )

    def get_cypher(self, query: str, added_values: list[str] = None) -> dict:
        data = {"query": query}
        return self.__post_with_added_values("/cypher", data, added_values)

    def get_artifact(
        self, group_id: str, artifact_id: str, added_values: list[str] = None
    ) -> dict:
        return self.__post_artifact(group_id, artifact_id, added_values)

    def get_artifact_releases(
        self, group_id: str, artifact_id: str, added_values: list[str] = None
    ) -> dict:
        return self.__post_artifact(
            "/artifact/releases", group_id, artifact_id, added_values
        )
