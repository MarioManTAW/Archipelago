from typing import Any, Dict
from zipfile import ZipFile

from worlds.Files import APPatch


class MarioSuperSluggersPatch(APPatch):
    game = "Mario Super Sluggers"
    patch_file_ending = ".apmss"
    data: str

    def get_manifest(self) -> Dict[str, Any]:
        manifest = super().get_manifest()
        manifest["patch_version"] = 1
        return manifest
    
    def write_contents(self, opened_zipfile: ZipFile) -> None:
        super().write_contents(opened_zipfile)
        opened_zipfile.writestr("mss.json", self.data)