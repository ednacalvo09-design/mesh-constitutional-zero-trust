"""
MESH — Invariantes Constitucionais Evolutivos
Define as regras fundamentais de execução do framework.
Regra combinada: Estes invariantes pertencem à Constituição, portanto
são EVOLUTIVOS e versionáveis. O que é IMUTÁVEL é o histórico de eventos
(event-store), que registra de forma fiel e auditável o que já aconteceu.
"""

from typing import Dict, Any, List

class ConstitutionInvariant:
  """Regra fundamental evolutiva do sistema MESH."""
  
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
    Valida se uma ação proposta viola algum invariante evolutivo.
    Retorna uma lista de violações encontradas.
    Nota: Esta lista de proibições pode ser aperfeiçoada em versões futuras da Constituição.
    """
    violations = []
    payload = str(action.get("payload", "")).lower()

    # Invariante 1: Proibição de comandos destrutivos (evolutivo - pode ganhar novas palavras)
    for cmd in ConstitutionInvariant.FORBIDDEN_COMMANDS:
      if cmd.lower() in payload:
        violations.append(f"VIOLAÇÃO CONSTITUCIONAL: Uso do comando proibido '{cmd}'.")

    # Invariante 2: Integridade de contexto (deve conter ID de auditoria para garantir histórico imutável)
    if "trace_id" not in action:
      violations.append("VIOLAÇÃO CONSTITUCIONAL: Ação sem 'trace_id' para rastreabilidade do histórico imutável.")

    return violations
