from translator.dev_llm_common import commonllmdev


class TS(commonllmdev):
    target_url = "https://chat.deepseek.com/"
    jsfile = "commonhookxhrstream.js"
    function1 = "url.endsWith('v0/chat/completion')"
    function2 = r"""if(!!(chunk.choices[0].delta.content))
                        thistext += chunk.choices[0].delta.content"""

    textarea_selector = "#chat-input"
    button_selector = 'div[role="button"]'
