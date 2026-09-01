"""
MESH - Fundação Alicerce - Constitution Package
Este pacote contém a Constituição EVOLUTIVA do MESH.
Regra: Constituição = Evolutiva e aperfeiçoável
       Histórico (event-store) = Imutável e fiel
"""

from .constitution import Constitution
from .invariants import ConstitutionInvariant
from .verifier import ConstitutionVerifier

__all__ = ["Constitution", "ConstitutionInvariant", "ConstitutionVerifier"]
