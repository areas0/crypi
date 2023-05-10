{
  description = "Crypi";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-22.11";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
        stdenv = pkgs.stdenv;
        pythonWithPackages = pkgs.python310.withPackages (ps: with ps; [
          pip
          django
          (
            buildPythonPackage rec {
              pname = "mpyc";
              version = "0.9";
              src = fetchPypi {
                inherit pname version;
                sha256 = "sha256-K3dszEVKPfTwHYyeW2cLlSixT+e/TRbNOm4xCdtrC4Y=";
              };
              doCheck = false;
              propagatedBuildInputs = [
                pkgs.python310Packages.numpy
                pkgs.python310Packages.gmpy2
              ];
            }
          )
        ]);
      in
      rec {
        builtPackages = flake-utils.lib.flattenTree
          {
            "crypi" = stdenv.mkDerivation
              {
                pname = "crypi";
                version = "1.0";
                src = ./.;
                nativeBuildInputs = [
                  pkgs.hello
                ];
              };
          };
        defaultPackage = builtPackages."crypi";
        devShell = pkgs.mkShell.override { inherit stdenv; } {
          inputsFrom = [ builtPackages."crypi" ];
          packages = [
            pythonWithPackages
          ];
        };
      }
    );
}
