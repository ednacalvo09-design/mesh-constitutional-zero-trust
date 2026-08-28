"""
MESH v5.0 — Invariantes Constitucionais Imutáveis
Define as regras invioláveis de execução do framework.
"""

from typing import Dict, Any, List

class ConstitutionInvariant:
    """Regra inviolável do sistema MESH v5.0."""
    
    FORBIDDEN_COMMANDS = [
        "rm -rf /",
        "format",
        "DROP DATABASE",
        "DELETE FROM",
        "sudo rm"
    ]

    @staticmethod
    def validate_action(action: Dict[str, Any]) -> List[str]:
        """
        Valida se uma ação proposta viola algum invariante.
        Retorna uma lista de violações encontradas.
        """
        violations = []
        payload = str(action.get("payload", "")).lower()

        # Invariante 1: Proibição de comandos destrutivos
        for cmd in ConstitutionInvariant.FORBIDDEN_COMMANDS:
            if cmd.lower() in payload:
                violations.append(f"VIOLAÇÃO CONSTITUCIONAL: Uso do comando proibido '{cmd}'.")

        # Invariante 2: Integridade de contexto (deve conter ID de auditoria)
        if "trace_id" not in action:
            violations.append("VIOLAÇÃO CONSTITUCIONAL: Ação sem 'trace_id' para rastreabilidade imutável.")

        return violations
