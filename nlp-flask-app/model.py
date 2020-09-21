from transformers import BartForConditionalGeneration, BartTokenizerFast
import torch
import time

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


class SummarizationModel:
    def __init__(self):
        self.model = BartForConditionalGeneration.from_pretrained(
            "facebook/bart-large-cnn"
        )
        self.model.half()
        self.model.to(device)
        self.model.eval()
        self.tokenizer = BartTokenizerFast.from_pretrained("facebook/bart-large-cnn")

    def summarize(
        self, text, num_beams=5, min_length=100, max_length=250, length_penalty=1.0
    ):
        encoded = self.tokenizer.encode(
            text, return_tensors="pt", max_length=1024, truncation=True
        ).to(device)
        summary_encoded = self.model.generate(
            input_ids=encoded,
            attention_mask=torch.IntTensor([[1] * len(encoded[0])]).to(device),
            max_length=max_length,
            min_length=min_length,
            length_penalty=length_penalty,
            num_beams=num_beams,
            early_stopping=True,
        )
        summarized_text = self.tokenizer.decode(
            summary_encoded[0].tolist(), skip_special_tokens=True
        )

        return summarized_text


def download_model():
    model = SummarizationModel()
    del model


if __name__ == "__main__":
    start = time.time()
    model = SummarizationModel()
    print(f"Model loaded in {round(time.time() - start, 4)}s")

    sample_input = """New York (CNN Business)Workers worry that in the not-too-distant future they will be sidelined by humans implanted with performance-enhancing microchips.Two-thirds of employees believe that in 2035, humans with chips implanted in their bodies will have an unfair advantage in the labor market, according to a Citrix survey of employees in the United States and Europe that was shared exclusively with CNN Business.Although cyborgs may sound like the stuff of science fiction, they could be here before long. Thousands of people in Sweden have inserted microchips in their hands that could one day replace keys and cards. Elon Musk recently showed off a working brain implant in pigs made by Neuralink, his brain-computer interface company. And Synchron, a San Francisco startup funded in part by the US Defense Department, is already testing an implantable wireless device that can stimulate the nervous system from the inside of a blood vessel. It has been implanted in patients with upper-limb paralysis.There is a sharp divide between employees and C-Suite executives over the pros and cons of implanted chips. And that gap echoes a broader difference of opinion between workers and leaders over artificial intelligence and the future of technology and the role of workers at the nexus of the two."Leaders are consistently more positive about the benefits that technology and AI will bring, while workers are more skeptical and concerned about their own role in the changing world of work," according to Citrix Work 2035, a research study done by the software company whose Workspace service helps employees to work from anywhere. Seventy-seven percent of business leaders believe that under-the-skin chips and sensors will boost worker performance and productivity by 2035. By comparison, just 43% of workers share that positive view on chips. "I look at it much less as a Hollywood-version of cyborgs," Citrix (CTXS) CEO David Henshall told CNN Business. "I see it more concentrated in wearables. You can imagine someone at a job site with augmented reality who can overlay a schematic diagram."AI will soon overtake humans in revenue generationAlthough employees seem more fearful of implanted devices, they may also be more likely to embrace them — perhaps if only in an effort to protect their livelihoods.Fifty-seven percent of workers would be willing to have chips implanted in their own bodies — if they felt it was safe and would boost their performance, the Citrix survey found. By contrast, only 31% of business leaders were open to implants themselves.Broadly, CEOs and employees agree that technology, especially artificial intelligence, will play a critical role in the future.In fact, 72% of professionals (workers and business leaders combined) polled by Citrix believe that by 2030 AI will replace humans as their organization's top revenue generator. And by 2035, AI technology investment will be the biggest driver of growth for their organization, according to 90% of business leaders. But what do these trends portend for humans?"We are already in the midst of the greatest winner-take-all economy in the history of the world. AI will drive those inequities up, not down," former Democratic presidential candidate Andrew Yang told CNN Business. Yang, whose signature issue is a $1,000-a-month universal basic income for all adults, said that if CEOs see more value coming from AI, they will devote fewer resources to humans. "Workers are getting replaced and automated in everything from meatpacking factories to accounting firms. Over time, you will have fewer workers," said Yang, who is a CNN political commentator. "We need to be more clear-eyed and realistic about what this means for our society," Workers share those concerns.Sixty percent of employees surveyed by Citrix think that by 2035, permanent employees will be a rarity.'Robots are not going to replace humans'The good news is that C-Suite executives, presumably the ones making the decisions, are much more bullish on the role of humans in the future. Most leaders (81%) think permanent employees will still have a place by 2035.Moreover, 70% of business leaders polled by Citrix said the pandemic made them believe human workers are more important to their business relative to technology.And it's easy to see how technology will continue to make employees better at their jobs, just as PCs, smartphones and the internet have.By 2035, technology such as AI personal assistants and augmented reality glasses will make workers at least twice as productive, according to 51% of professionals in the Citrix survey."Robots are not going to replace humans," Henshall, the Citrix CEO, said. "Technology will make people better and smarter. It's an enabler, not a replacer."Yet it seems likely that technology, especially AI, will shift the role that humans play in companies in the future.Eighty-three percent of professionals say that by 2035, technology will automate low-value tasks. In theory, that would free up workers to focus on more meaningful work. "Technology over the last 100 years has done nothing but help people become more productive and efficient," said Henshall. "The types of tasks will have to evolve over time."Will AI eventually replace the C-Suite?But there is no guarantee that the humans being "freed" from mundane tasks will be the same ones hired for the more exciting work. Countless workers, especially those without the right skills training, could be left behind in the disruption."The workers that will suffer the most will be the majority whose work can be automated away," said Yang. "There will be a handful of executives and investors who end up profiting at unprecedented levels."Yang pointed out that Google recently launched an AI call center that will enable companies to push some of their customer service calls to Google instead of their own workers. He noted more than 2 million Americans work in call centers — and predicted that most companies will not shift those workers to other positions."That's not how organizations function," said Yang, whose devoted following during the presidential campaign was known as the Yang Gang. "They will say, 'You are no longer needed, thank you for your service. Here's a week's severance.'"Management may not be immune to the coming wave of disruption, either. The Citrix survey found that most professionals believe that in the future, organizations will have a central AI department that oversees all areas of business. Even CEOs will work in a human-machine tandem with an office of chief artificial intelligence.Not just that, but more than half (57%) of all professionals believe that by 2035, there will be no traditional leadership team at all — just AI making most business decisions.Perhaps that will boost the CEO ranks in the Yang Gang."""

    start = time.time()
    output_text = model.summarize(sample_input)
    reduction = 1 - len(output_text) / len(sample_input)
    print(
        f"---------------------------------Summarization took {round(time.time() - start, 2)}s at {round(reduction, 4) * 100}% reduction---------------------------------"
    )
    print(output_text)